from argparse import ArgumentParser

class Converter:
    def __init__(self):
        self.parser = ArgumentParser(description="Weight Converter - Options")
        self.parser.add_argument('-kg', '--kilograms', type=float, default=None)
        self.parser.add_argument('-lb', '--pounds', type=float, default=None)

    def convert(self) -> str:
        if self.parser.parse_args().kilograms == None and self.parser.parse_args().pounds != None:
            return f"{self.parser.parse_args().pounds} lb = {(self.parser.parse_args().pounds * 0.4535924)} kg"
        elif self.parser.parse_args().kilograms != None and self.parser.parse_args().pounds == None:
            return f"{self.parser.parse_args().kilograms} kg = {(self.parser.parse_args().kilograms * 2.204623):.02f} lb"
        else:
            return "Only youse one flag"


if __name__ == "__main__":
    converter = Converter()
    print(converter.convert())