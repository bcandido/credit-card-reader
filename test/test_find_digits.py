import pytest

import opencv
from credit_card_reader import CreditCardReader


@pytest.mark.parametrize("image", [
    'assets/credit-card.png',
    'assets/credit_card_01.png',
    'assets/credit_card_02.png',
    'assets/credit_card_03.png',
    'assets/credit_card_04.png',
    'assets/credit_card_05.png',
    'assets/credit-card_06.jpeg',
    'assets/credit-card_07.jpeg',
    'assets/credit_card_08.png',
    'assets/credit_card_09.jpg'
])
def test_find_card_digits_groups(image):
    image = opencv.load_image(image)

    reader = CreditCardReader(image)
    reader.detect()
