#With user input text create morse Code
#One Class for all Converters
# oop for qr-code

from morse_constants import MENU_INSTRUCTIONS, ERROR_MESSAGE, CHARS_TO_MORSE, MORSE_TO_CHARS

def encrypt(user_inputent: str) -> str:
    output: str = ""
    for key in list(user_inputent.upper()):
        try:
            output += CHARS_TO_MORSE[key]
            if key != user_inputent[-1]:
                output += " "
        except:
            output += "\\"
            if key != user_inputent[-1]:
                output += " "
        return output

def decrypt(user_inputde: str) -> None:
    output: str = ""
    for key in user_inputde.split(" "):
        output += MORSE_TO_CHARS[key]
    return output

if __name__ == "__main__": 
    user_input: str = input(MENU_INSTRUCTIONS)
    match user_input:
        case "1":
            encrypt_input:str = input("Please enter a Text to convert to morse code: ")
            print(encrypt(encrypt_input))
        case "2":
            decrypt_input:str = input("Please enter a morse code to decrypt: ")
            print(decrypt(decrypt_input))
        case _:
            print(ERROR_MESSAGE)