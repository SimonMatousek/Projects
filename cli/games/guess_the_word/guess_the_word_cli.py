from random import choice
from string import ascii_uppercase

LIVES: int = 5
WORDS: list[str] = ["Tina",
"apple", "banana", "cat", "dog", "elephant", "flower", "guitar", "house", "jacket", "kite", "lemon",
"mountain", "notebook", "orange", "penguin", "queen", "rainbow", "sun", "tree", "umbrella", "violin",
"water", "xylophone", "yacht", "zebra", "airplane", "book", "car", "dance", "egg", "fish", "game", "hat",
"island", "juice", "key", "lamp", "moon", "nest", "ocean", "pizza", "quilt", "robot", "star", "table",
"unicorn", "vase", "window", "yarn", "ant", "bear", "cloud", "drum", "eagle", "fox", "grass", "horse",
"insect", "jelly", "kiwi", "leaf", "mouse", "nut", "owl", "parrot", "quokka", "rose", "snake", "turtle",
"umbrella", "volcano", "whale", "x-ray", "yo-yo", "zipper", "almond", "bread", "cucumber", "doughnut",
"eggplant", "fig", "grape", "honey", "iceberg", "jellyfish", "kiwi", "lollipop", "mushroom", "noodle",
"olive", "pancake", "quinoa", "radish", "spinach", "tofu", "turnip", "vanilla", "waffle", "zucchini",
"adventure", "bicycle", "candle", "dolphin", "elephant", "feather", "giraffe", "horizon", "igloo",
"jungle", "kettle", "lighthouse", "mosaic", "nectar", "octopus", "pyramid", "quasar", "robot", "sapphire",
"telescope", "universe", "vortex", "whisper", "xenon", "yarn", "zodiac", "artichoke", "butterfly", "cactus",
"daisy", "eclipse", "fountain", "goblet", "hammock", "ink", "jigsaw", "kaleidoscope", "lunar", "mystery",
"ninja", "oasis", "puzzle", "quilt", "raccoon", "symphony", "tulip", "ukulele", "village", "wisteria", 
"xylophonist", "yeti", "zinnia"]

WORD_EXAMPLE: str = WORDS[-1]

def get_word(words: list[str]) -> str:
    word: str = choice(words)
    return word

def play() -> None:
    print("Explanation")
    word: str = get_word(WORDS).upper()
    letters_word: set[str] = set(word.upper())
    abc: set[str] = set(ascii_uppercase)
    used_letters: set[str] = set()
    life: int = LIVES
    
    while life > 0 and len(letters_word) > 0:
        print(f"Lives: {life}")
        print(f"Letters used: {"".join(used_letters)}")
        word_list_print: list[str] = [letter if letter in used_letters else "_ " for letter in word]
        print(f"Word: {"".join(word_list_print)}")
        user_letter_input: str = input("Guess a letter: ")
        user_letter = user_letter_input.upper()
        # IF the user_letter is a letter
        if user_letter in abc - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters_word:
                letters_word.remove(user_letter)
                print("Correct Guess!")
            else:
                life -= 1
                print("Wrong Guess ... try again!")
        elif user_letter in used_letters:
            print("Already used... ")
        else:
            print("Try again!")
        
            
        
    if life == 0:
        print("Lost")
    else:
        print("Win")

if __name__ == "__main__":
    play()