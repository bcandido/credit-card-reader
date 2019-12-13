import cv2
import imutils


def load_image(image_path):
    """
    Load image based on system path
    :param image_path:
    :return:
    """
    return cv2.imread(image_path)


def convert_to_gray_scale(image, resize_width=300):
    """
    From the input image, resize it, and convert it to grayscale
    :param image:
    :param resize_width: default 300
    :return: gray scale image resized
    """
    image = imutils.resize(image, width=resize_width)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def show(image):
    """
    Simply show an image
    Blocks execution until press any key
    :param image:
    :return:
    """
    cv2.imshow("Showing image", image)
    cv2.waitKey(0)
