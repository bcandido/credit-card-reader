import opencv
from cli import CommandLineParser


def main():
    args = parser_arguments()

    image = opencv.load_image(args.image)

    # initialize a rectangular kernel
    rect_kernel = opencv.get_morphology_rect(size=(9, 3))

    # Find light regions against a dark background (i.e., credit card numbers)
    gray = opencv.convert_to_gray_scale(image)
    tophat = opencv.morphology_tophat(gray, rect_kernel)

    opencv.show(tophat)


def parser_arguments():
    cli = CommandLineParser()
    return cli.parse()


if __name__ == '__main__':
    main()
