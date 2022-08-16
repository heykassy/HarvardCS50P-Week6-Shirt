from sys import argv, exit
from PIL import Image, ImageOps
from os import path


def main():

    extensions = (".jpeg", ".jpg", ".png")

    filename1, fileext1 = path.splitext(argv[1])
    filename2, fileext2 = path.splitext(argv[2])

    # Expects the user to provide two command-line arguments:
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    elif not fileext1.lower() in extensions or not fileext2.lower() in extensions:
        exit("Invalid input")
    elif fileext1 != fileext2:
        exit("Input and output have different extensions")

    try:
        overlay_shirt(argv[1], argv[2])
    except FileNotFoundError:
        exit(f"File {argv[1]} doesn't exist")


def overlay_shirt(image, outputfilename):
    image = Image.open(image)
    shirt = Image.open("shirt.png")
    size = shirt.size
    output = ImageOps.fit(image, size)
    output.paste(shirt, shirt)
    output.save(outputfilename)


if __name__ == "__main__":
    main()
