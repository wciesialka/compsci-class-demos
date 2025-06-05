# Import our command-line interface module.
import cli
# Import our key-generation module
import keygen
# Import our word-scrambling module
import scramble
# Import deepcopy to make "deep copies" of dictionaries
from copy import deepcopy

class UserQuitException(SystemExit):
    def __init__(self):
        super().__init__()
        self.code = 0

class WordScramblerDriver:

    def __init__(self):
        self.__key = None
    
    @property
    def key(self):
        return deepcopy(self.__key)

    def get_key(self):
        choice = cli.key_menu()
        if choice == cli.KeyMenuChoice.GENERATE_NEW_KEY:
            self.__key = keygen.generate_random_key()
        elif choice == cli.KeyMenuChoice.IMPORT_KEY:
            key_string = input("Your key: ")
            self.__key = keygen.decode_key(key_string)
        raise UserQuitException
    
    def scramble_menu(self):
        choice = cli.scramble_menu()
        if choice == cli.ScrambleMenuChoice.SCRAMBLE_MESSAGE:
            word = cli.get_user_message()
            scrambled = scramble.scramble(word, self.key)
            return f"Your scrambled message: \"{scrambled}\""
        elif choice == cli.ScrambleMenuChoice.UNSCRAMBLE_MESSAGE:
            word = cli.get_user_message()
            unscrambled = scramble.unscramble(word, self.key)
            return f"Your unscrambled message: \"{unscrambled}\""
        elif choice == cli.ScrambleMenuChoice.EXPORT_KEY:
            key_string = keygen.encode_key(self.key)
            return f"Your key: \"{key_string}"
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Goodbye!")
    else:
        message = "[Press ENTER to exit.]"
        input(f"{message:^80}")