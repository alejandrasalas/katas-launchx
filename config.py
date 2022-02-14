"""
def main():
    try:
        configuration = open('config.txt2')
    except FileNotFoundError:
        print("¡No se encuentra el archivo!")


if __name__ == '__main__':
    main()


def main():
    try:
        configuration = open('config.txt2')
    except Exception:
        print("¡No se encuentra el archivo!")
"""

def main():
    try:
        configuration = open('config.txt2')
    except FileNotFoundError:
        print("¡No se encuentra el archivo!")
    except IsADirectoryError:
        print("El archivo es un directorio")
    except PermissionError:
        print("No teiens permiso para acceder al directorio")


if __name__ == '__main__':
    main()