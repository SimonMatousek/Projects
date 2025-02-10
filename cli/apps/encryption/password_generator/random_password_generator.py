from random import shuffle, choice
from string import ascii_letters, digits, punctuation
#TODO: oop


"""
    - Letter: (A-Z) or (a-z)
    - Numbers: (0-9)
    - Punctuation: !"&%$/
    """

class Password_generator():
    def __init__(self):
        self.password = ""

    def generate(self) -> str:
        try:
            length: int = int(input("Please input password length: "))
        except:
            return"Something went wrong."
        if length < 1:
            return "Only positive password length is accepted"
        characters: list = list(ascii_letters + digits + punctuation)
        password_list: list = [choice(characters) for _ in range(length)]
        return "".join(password_list)


def run() -> str:
    password_gen = Password_generator()
    print(password_gen.generate())


if __name__ == "__main__":
    run()
