import cv2
import imutils
import numpy

GRADIENT_TYPE_UINT_8 = "uint8"


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


def resize(image, width=None, height=None):
    """
    Resize image
    :param image:
    :param width:
    :param height:
    :return:
    """
    return imutils.resize(image, width=width, height=height)


def show(image):
    """
    Simply show an image
    Blocks execution until press any key
    :param image:
    :return:
    """
    cv2.imshow("Showing image", image)
    cv2.waitKey(0)


def morphology_tophat(image, kernel):
    """
    Apply a Tophat (white hat) morphological operator.
    :param image:
    :param kernel:
    :return:
    """
    return cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)


def morphology_close(image, kernel):
    """
    Apply a Tophat (white hat) morphological operator.
    :param image:
    :param kernel:
    :return:
    """
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)


def apply_otsus_threshold(image, minVal, maxVal):
    """
    Apply Otsu's threshold to binarize image
    :param image:
    :param minVal:
    :param maxVal:
    :return:
    """
    return cv2.threshold(image, minVal, maxVal, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


def get_morphology_rect(size):
    """
    Get Structuring Kernel
    :param size:
    :return:
    """
    return cv2.getStructuringElement(cv2.MORPH_RECT, size)


def apply_scharr_gradient(image, dx, dy):
    """
    Apply Scharr Gradient on an Image
    :param image:
    :param dx:
    :param dy:
    :return:
    """
    return cv2.Sobel(image, ddepth=cv2.CV_32F, dx=dx, dy=dy, ksize=-1)


def normalize_gradient(gradient, type):
    """
    Normalize Gradient image
    :param gradient:
    :param type:
    :return:
    """
    normalized_gradient = numpy.absolute(gradient)
    (minVal, maxVal) = (numpy.min(normalized_gradient), numpy.max(normalized_gradient))
    scaled = scale_gradient(normalized_gradient, minVal, maxVal, 255)
    return scaled.astype(type)


def scale_gradient(gradient, min_val, max_val, scale):
    """
    Scale gradient image
    :param gradient:
    :param min_val:
    :param max_val:
    :param scale:
    :return:
    """
    return scale * ((gradient - min_val) / (max_val - min_val))


def grab_contours(image):
    """
    Grab image contours for a given image
    :param image:
    :return:
    """
    contours = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return imutils.grab_contours(contours)


def get_bounding_rect(contour):
    """
    Get bounding box of the contour.
    :param contour:
    :return:
    """
    (x, y, w, h) = cv2.boundingRect(contour)
    return x, y, w, h


def draw_rectangle(image, point_1, point_2, color, thickness=None, lineType=None, shift=None):
    """
    Draw rectangle for a given image
    :param image:
    :param point_1:
    :param point_2:
    :param color:
    :param thickness:
    :param lineType:
    :param shift:
    :return:
    """
    cv2.rectangle(image, point_1, point_2, color, thickness, lineType, shift)
