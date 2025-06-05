# Import Enum class from enum module to create an Enumerable
from enum import Enum

# Create a key menu enum
def KeyMenuChoice(Enum):
    GENERATE_NEW_KEY = 1
    IMPORT_KEY = 2
    QUIT = 3

def ScrambleMenuChoice(Enum):
    SCRAMBLE_MESSAGE = 1
    UNSCRAMBLE_MESSAGE = 2
    NEW_KEY = 3
    EXPORT_KEY = 4
    QUIT = 5

def key_menu():
    choices = {
        "1": KeyMenuChoice.GENERATE_NEW_KEY,
        "2": KeyMenuChoice.IMPORT_KEY,
        "3": KeyMenuChoice.QUIT
    }
    print("Welcome to Word Scrambler!")
    print("No key currently loaded.")
    print("Actions:")
    print("\t[1] Generate new key.")
    print("\t[2] Import key.")
    print("\t[3] Exit.")
    choice = input("Your choice: ").strip()
    if choice in choices:
        return choices[choice]
    print(f"Invalid option: \"{choice}\"")
    print("Please try again.")
    return key_menu()

def scramble_menu():
    choices = {
        "1": ScrambleMenuChoice.SCRAMBLE_MESSAGE,
        "2": ScrambleMenuChoice.UNSCRAMBLE_MESSAGE,
        "3": ScrambleMenuChoice.NEW_KEY,
        "4": ScrambleMenuChoice.EXPORT_KEY,
        "5": ScrambleMenuChoice.QUIT
    }
    print("Actions:")
    print("\t[1] Scramble message.")
    print("\t[2] Unscramble message.")
    print("\t[3] Generate/import new key.")
    print("\t[4] Export key.")
    print("\t[5] Exit.")
    print()
    choice = input("Your selection: ").strip()
    if choice in choices:
        return choices[choice]
    print(f"Invalid option: \"{choice}\"")
    print("Please try again.")
    return scramble_menu()

def get_user_message():
    return input("Your message: ").strip()