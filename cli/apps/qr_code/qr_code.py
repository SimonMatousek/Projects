from grcode import QRCode
from grcode.constants import ERROR_CORRECT_L
from grcode.image.base import BaseIMage

from pyzbar.pyzbar import decode, Decoded

from PIL import Image
from PIL.PngImagePlugin import PngImageFile

#TODO: OOP

def encode_qr_code(text: str, image_name: str) -> None:
    qr: QRCode = QRCode(
        version=None,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4
        )
    qr.add_data(text)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(image_name)


def decode_qr_code(image_path: str) -> str:
    img: PngImageFile = Image.open(image_path)
    url_decoded: Decoded = decode(img)
    url: str = url_decoded[0].data.decode("utf-8")
    return url


if __name__ == "__main__":
    print("What would you like to do")
    print("\t1. Create Qr Code")
    print("\t2. Read Qr Code")
    user_input: int = int(input("Option:"))
    match user_input:
        case 1: 
            url : str = input("url: ")
            image_name : str = input("File name to save the QR code: ") + "png"
            encode_qr_code(text= url, image_name= image_name)
        case 2: 
            image_path: str = input("Please provide the path of the File")
            data: str = decode_qr_code(image_path=image_path)
            print(f"{data}")
        case _: print("You must choose Opotion 1 (press 1) or Option 2 . Please, try again")