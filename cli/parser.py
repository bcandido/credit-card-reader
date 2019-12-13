import argparse
from attribute_dict import AttributeDict


class CommandLineParser:
    parser = None

    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def parse(self):
        self._add_arguments()
        return AttributeDict(vars(self.parser.parse_args()))

    def _add_arguments(self):
        self.parser.add_argument('-i', '--image', required=True, help='path to credit card image')
