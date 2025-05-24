import sys
import time
import convert


def main():
    # Verifica si se ha proporcionado un argumento
    if len(sys.argv) < 2:
        print("Uso: python main.py <path>")
        sys.exit(1)

    # Obtiene el path del archivo desde los argumentos
    file_path = sys.argv[1]
    start = time.time()

    # Intenta abrir y leer el archivo
    try:
        convert.convert_to_webp(file_path)
        elapsed = time.time()
        print(f"El archivo {file_path} ha sido convertido a WebP.")
        print(f"Done in {start - elapsed} seconds")

    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()
