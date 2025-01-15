from argparse import ArgumentParser
MIL_2_KM = 1.60934

parser = ArgumentParser(description="Distance Converter - Options")
parser.add_argument('--distance_in_miles', type = float, help= "Distance in miles")

arguments = parser.parse_args()
distance_mil = arguments.distance_in_miles
distance_km = distance_mil * MIL_2_KM

print(f"{arguments.distance_in_miles:.02f} mil = {arguments.distance_in_miles * 1.609340:.02f}")



