import sys
import time
import convert
import argparse


def main():
    parser = argparse.ArgumentParser(description="Convert SVG to WebP")

    parser.add_argument("file_path", help="Path to the input SVG file")
    parser.add_argument("--res", help="Output resolution as WIDTH,HEIGHT (e.g. 800,600)", default=None)
    parser.add_argument("--quality", help="Quality for output WebP (0-100)", type=int, default=85)

    args = parser.parse_args()

    output_size = None
    if args.res:
        try:
            width, height = map(int, args.res.split(","))
            output_size = (width, height)
        except ValueError:
            parser.error("Resolution must be in the format WIDTH,HEIGHT where both are integers")

    quality = args.quality

    file_path = args.file_path
    opts = {
        "file_path": args.file_path,
        "output_size": output_size,
        "quality": quality,
    }
    print(opts)
    
    start = time.time()
    try:
        if file_path.lower().endswith(".svg"):
            convert.svg_to_webp(**opts)
        else:
            convert.convert_to_webp(**opts)
        elapsed = time.time()
        print(f"El archivo {file_path} ha sido convertido a WebP.")
        print(f"Done in {start - elapsed} seconds")

    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()
