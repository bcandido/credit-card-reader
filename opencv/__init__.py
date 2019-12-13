import os, sys
from opencv.utils import convert_to_gray_scale
from opencv.utils import show
from opencv.utils import load_image

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
))