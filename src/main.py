import opencv
from credit_card_reader import CreditCardReader
from parser import CommandLineParser


def main():
    cli = CommandLineParser()
    args = cli.parse()

    image = opencv.load_image(args.image)

    reader = CreditCardReader(image)
    reader.detect()


if __name__ == '__main__':
    main()
