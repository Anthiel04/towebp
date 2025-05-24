from PIL import Image
import os


def convert_to_webp(file_path):
    img = Image.open(file_path)
    if file_path.lower().endswith(".png"):
        img.save(file_path.rsplit(".", 1)[0] + ".webp", "webp", lossless=True)
    else:
        img = img.convert("RGB")  # WebP no soporta transparencia en modo RGBA
        img.save(file_path.rsplit(".", 1)[0] + ".webp", "webp", quality=85)
