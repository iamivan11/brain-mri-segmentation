import matplotlib.pyplot as plt


def visualize_slice(img, s=0, cap="", cmap="jet"):
    """Show a single slice from a volume/image."""
    plt.figure(figsize=(6, 6))
    plt.imshow(img[:, :, s], cmap=cmap)
    plt.title(f"{cap} Slice {s + 1}")
    plt.axis("off")
    plt.show()


def visualize_row(img, cap="", cmap="jet"):
    """Show a single row of slices for the provided image/volume."""
    n_slices = img.shape[-1]
    _, axes = plt.subplots(1, n_slices, figsize=(4 * n_slices, 4))
    if n_slices == 1:
        axes = [axes]
    for i in range(n_slices):
        axes[i].imshow(img[..., i], cmap=cmap)
        axes[i].axis("off")
        axes[i].set_title(f"{cap} Slice {i + 1}")
    plt.tight_layout()
    plt.show()


def visualize_rows(
    img1,
    img2,
    img3,
    cap_1="",
    cap_2="",
    cap_3="",
    cmap_1="jet",
    cmap_2="jet",
    cmap_3="jet",
):
    """Show rows of slices for img1 (e.g. T1), img2 (e.g. GT), img3 (e.g. segmented)."""
    z = img2.shape[-1]
    _, axes = plt.subplots(3, z, figsize=(3 * z, 8))
    for i in range(z):
        axes[0, i].imshow(img1[..., i], cmap=cmap_1)
        axes[0, i].axis("off")
        axes[0, i].set_title(f"{cap_1} Slice {i + 1}")
        axes[1, i].imshow(img2[..., i], cmap=cmap_2)
        axes[1, i].axis("off")
        axes[1, i].set_title(f"{cap_2} Slice {i + 1}")
        axes[2, i].imshow(img3[..., i], cmap=cmap_3)
        axes[2, i].axis("off")
        axes[2, i].set_title(f"{cap_3} Slice {i + 1}")
    plt.tight_layout()
    plt.show()
