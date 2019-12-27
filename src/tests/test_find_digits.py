import pytest

import opencv
from credit_card_reader import CreditCardReader


@pytest.mark.parametrize("image", [
    '../resources/credit_card.png',
    '../resources/credit_card_01.png',
    '../resources/credit_card_02.png',
    '../resources/credit_card_03.png',
    '../resources/credit_card_04.png',
    '../resources/credit_card_05.png',
    '../resources/credit_card_06.jpeg',
    '../resources/credit_card_07.jpeg',
    '../resources/credit_card_08.png',
    '../resources/credit_card_09.jpg'
])
def test_find_card_digits_groups(image):
    image = opencv.load_image(image)

    reader = CreditCardReader(image)
    reader.detect()
