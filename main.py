import opencv
from cli import CommandLineParser


def main():
    args = parser_arguments()

    image = opencv.load_image(args.image)
    gray = opencv.convert_to_gray_scale(image)
    opencv.show(gray)


def parser_arguments():
    cli = CommandLineParser()
    return cli.parse()


if __name__ == '__main__':
    main()
