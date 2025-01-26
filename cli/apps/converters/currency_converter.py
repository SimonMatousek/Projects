from argparse import ArgumentParser

CZK_2_EURO:float = 0.0397
EURO_2_CZK:float = 25.2158

def boolean_string(s):
    return s == "True"
parser = ArgumentParser(description="Currency Converter - Options")
parser.add_argument('-a', type=float, help="Total amount of money", default=1.0)
parser.add_argument('-c', type= boolean_string, help="Change czk to euro if True", default=False)
parser.add_argument('-e', type= boolean_string, help="Change euro to czk if True", default=True)



arguments = parser.parse_args()

money: float = arguments.a
is_czk: bool = arguments.c
is_euro: bool = arguments.e

converted_amount: float = 0


if is_euro:
    converted_amount = money * EURO_2_CZK
    print(f"{money} euro = {converted_amount}")
elif is_czk:
    converted_amount = money * CZK_2_EURO
    print(f"{money} czk = {converted_amount}")
else:
    print("something went wrong")
"""
10 < 100 -> true
0,"",None,0.0,[] -> all false    
    """
