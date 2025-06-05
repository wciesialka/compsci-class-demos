# Import Dict from Typing module for type-hinting
from typing import Dict

def scramble(word: str, key: Dict[str, str]):
    result = ""
    # Build the result character by character
    for character in word:
        # If the character is in our key, then add the corresponding
        # character to our list. Otherwise, just add the character.
        if character in key:
            result += key[character]
        else:
            result += character
    return result

def unscramble(word: str, key: Dict[str, str]):
    # Create a dictionary that puts the key in reverse,
    # then use that to "scramble" the word.
    reverse_key = {v: k for k, v in key.items()}
    return scramble(word, reverse_key)