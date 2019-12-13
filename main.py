from cli import CommandLineParser


def main():
    cli = CommandLineParser()
    args = cli.parse()
    print(args)


if __name__ == '__main__':
    main()
