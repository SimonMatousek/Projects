from argparse import ArgumentParser 
#°C = (°F - 32) × 5/9


def fahrenheit_to_celsius(temperature_fahrenheit: float) -> float:
    return (temperature_fahrenheit - 32) * 5/9

parser = ArgumentParser(description="Temperature Converter - Options")
parser.add_argument('-f', type=float, help="Temperature in Fahrenheit")

arguments = parser.parse_args()

temperature_f: float = arguments.fahrenheit
temperature_c: float = fahrenheit_to_celsius(temperature_f)

print(f"{temperature_f} F = {temperature_c} C")

#Debug Currency converter / 