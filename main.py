import opencv
from cli import CommandLineParser


def main():
    args = parser_arguments()

    image = opencv.load_image(args.image)

    # initialize a rectangular and square kernel
    rect_kernel = opencv.get_morphology_rect(size=(9, 3))
    square_kernel = opencv.get_morphology_rect(size=(5, 5))

    # Find light regions against a dark background (i.e., credit card numbers)
    gray = opencv.convert_to_gray_scale(image)
    tophat = opencv.morphology_tophat(gray, rect_kernel)

    # isolate digits
    grad_x = opencv.apply_scharr_gradient(tophat, dx=1, dy=0)
    grad_x = opencv.normalize_gradient(grad_x, opencv.GRADIENT_TYPE_UINT_8)

    # eliminate gaps in between credit card number digits
    grad_x = opencv.morphology_close(grad_x, rect_kernel)
    thresh = opencv.apply_otsus_threshold(grad_x, 0, 255)

    # apply close again for eliminate gaps
    thresh = opencv.morphology_close(thresh, square_kernel)

    # find grouped digits
    digits = opencv.find_digit_groups(thresh)
    print(digits)


def parser_arguments():
    cli = CommandLineParser()
    return cli.parse()


if __name__ == '__main__':
    main()
