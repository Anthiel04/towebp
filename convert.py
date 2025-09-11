from PIL import Image
import os
import cairosvg
from io import BytesIO

"""Args:
    file_path (str): Path to the input image.
    output_path (str, optional): Path to save the output WebP image.
        If None, saves in same directory with same base name.
    output_size (tuple, optional): (width, height) to resize the image to.
        If None, original size is kept.
    quality (int, optional): Compression quality for WebP (0-100).
        Default is 85.
"""


def convert_to_webp(file_path, output_size, quality):

    img = Image.open(file_path)

    # Resize if output size given, preserving aspect ratio
    if output_size:
        # Using thumbnail preserves aspect ratio
        img.thumbnail(output_size)

    # Convert mode for WebP: if PNG keep transparency, else convert to RGB
    if file_path.lower().endswith(".png"):
        # PNG may have transparency; save with lossless option
        save_params = {"lossless": True}
        if quality:
            save_params["quality"] = quality  # quality has no effect when lossless True
    else:
        # For other formats convert to RGB (no transparency)
        img = img.convert("RGB")
        save_params = {"quality": quality}

    file_path = file_path.rsplit(".", 1)[0] + ".webp"
    print("Saved to" + file_path)
    img.save(file_path, "webp", **save_params)


"""     img = Image.open(file_path)
        if file_path.lower().endswith(".png"):
            img.save(file_path.rsplit(".", 1)[0] + ".webp", "webp", lossless=True)
        else:
            img = img.convert("RGB")  # WebP no soporta transparencia en modo RGBA
            img.save(file_path.rsplit(".", 1)[0] + ".webp", "webp", quality=85)
 """


def svg_to_webp(file_path, output_size=None, quality=85):
    """
    Convert an SVG file to WebP format with optional resizing and quality.

    Args:
        file_path (str): Path to the input SVG file.
        output_size (tuple, optional): (width, height) for output image. Defaults to None (no resize).
        quality (int, optional): WebP quality from 0 to 100. Defaults to 85.
    """
    # Prepare CairoSVG kwargs ensuring numeric types
    cairosvg_kwargs = {}
    if output_size:
        cairosvg_kwargs["output_width"] = (
            int(output_size[0])
            if isinstance(output_size[0], (int, float, str))
            else output_size[0]
        )
        cairosvg_kwargs["output_height"] = (
            int(output_size[1])
            if isinstance(output_size[1], (int, float, str))
            else output_size[1]
        )

    # Convert SVG to PNG bytes
    png_data = cairosvg.svg2png(url=file_path, **cairosvg_kwargs)

    # Open PNG bytes as PIL image
    img = Image.open(BytesIO(png_data))

    # Resize using thumbnail to maintain aspect ratio, if output_size given
    if output_size:
        img.thumbnail((int(output_size[0]), int(output_size[1])))

    # Cast quality to int to avoid type errors
    quality_val = int(quality) if isinstance(quality, str) else quality

    # Save as WebP with specified quality, replacing original extension
    output_path = file_path.rsplit(".", 1)[0] + ".webp"
    img.save(output_path, "WEBP", quality=quality_val)
