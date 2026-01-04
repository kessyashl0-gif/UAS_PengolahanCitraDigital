import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def read_image(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File tidak ditemukan: {path}")

    img_bgr = cv2.imread(path)
    if img_bgr is None:
        raise ValueError("Gagal membaca gambar. Pastikan format file valid (jpg/png).")

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    return img_bgr, img_rgb, gray


def otsu_threshold(gray: np.ndarray) -> np.ndarray:
    # Otsu Thresholding (sesuai materi thresholding)
    _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return otsu


def sobel_magnitude(gray: np.ndarray) -> np.ndarray:
    # Sobel (Gx, Gy, magnitude)
    gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    mag = np.sqrt(gx**2 + gy**2)

    # normalisasi biar enak dilihat
    if mag.max() > 0:
        mag = (mag / mag.max() * 255).astype(np.uint8)
    else:
        mag = mag.astype(np.uint8)
    return mag


def canny_edges(gray: np.ndarray, t1: int = 100, t2: int = 200) -> np.ndarray:
    # Canny edge detection
    edges = cv2.Canny(gray, threshold1=t1, threshold2=t2, apertureSize=3)
    return edges


def watershed_segmentation(img_bgr: np.ndarray):
    """
    Watershed segmentation standar:
    1) Noise removal + threshold
    2) Sure background (dilate)
    3) Sure foreground (distance transform)
    4) Unknown region
    5) Connected components -> markers
    6) Apply watershed
    """
    # Konversi ke gray
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Noise removal
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold (Otsu) untuk mask awal
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Pastikan objek putih (kadang kebalik tergantung gambar)
    # Kalau objek dominan gelap, invert bisa membantu.
    # Heuristik sederhana: kalau putih terlalu sedikit, invert
    white_ratio = np.mean(thresh == 255)
    if white_ratio < 0.35:
        thresh = cv2.bitwise_not(thresh)

    # Morph opening (hapus noise kecil)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Sure background
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    # Sure foreground via distance transform
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    sure_fg = sure_fg.astype(np.uint8)

    # Unknown region
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Marker labelling
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    # Apply watershed
    ws_input = img_bgr.copy()
    markers = cv2.watershed(ws_input, markers)

    # Gambar boundary (markers == -1)
    result = img_bgr.copy()
    result[markers == -1] = [0, 0, 255]  # merah (BGR)

    return result, markers, thresh, opening, sure_bg, sure_fg, unknown


def show_results(img_rgb, gray, otsu, sobel_mag, canny, ws_bgr):
    ws_rgb = cv2.cvtColor(ws_bgr, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(14, 8))

    plt.subplot(2, 3, 1)
    plt.title("Original")
    plt.imshow(img_rgb)
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.title("Grayscale")
    plt.imshow(gray, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.title("Otsu Threshold")
    plt.imshow(otsu, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 3, 4)
    plt.title("Sobel Magnitude")
    plt.imshow(sobel_mag, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.title("Canny Edges")
    plt.imshow(canny, cmap="gray")
    plt.axis("off")

    plt.subplot(2, 3, 6)
    plt.title("Watershed (Boundary Merah)")
    plt.imshow(ws_rgb)
    plt.axis("off")

    plt.tight_layout()
    plt.show()


def main():
    # GANTI PATH GAMBAR DI SINI:
    image_path = "gambaruas.jpeg"  # contoh: "data/gambar.jpg"

    img_bgr, img_rgb, gray = read_image(image_path)

    # Metode segmentasi
    otsu = otsu_threshold(gray)
    sobel_mag = sobel_magnitude(gray)
    canny = canny_edges(gray, 100, 200)
    ws_result_bgr, markers, *_debug = watershed_segmentation(img_bgr)

    # Tampilkan hasil
    show_results(img_rgb, gray, otsu, sobel_mag, canny, ws_result_bgr)

    # (Opsional) Simpan output
    out_dir = "output"
    os.makedirs(out_dir, exist_ok=True)
    cv2.imwrite(os.path.join(out_dir, "otsu.png"), otsu)
    cv2.imwrite(os.path.join(out_dir, "sobel_mag.png"), sobel_mag)
    cv2.imwrite(os.path.join(out_dir, "canny.png"), canny)
    cv2.imwrite(os.path.join(out_dir, "watershed.png"), ws_result_bgr)

    print("Selesai! Output tersimpan di folder:", out_dir)


if __name__ == "__main__":
    main()
