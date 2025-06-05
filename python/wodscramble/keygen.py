# Import pickle and base64 modules for serialization
import pickle
import base64
# Import random module to generate our random key
import random
# Import string module for string operations
import string
# Import Dict from Typing module for type-hinting
from typing import Dict

# Seed the random number generator
random.seed()

def generate_random_key():
    # Create a list of letters, and a shuffled version of that list
    letters = string.ascii_letters + string.digits + string.punctuation + " "
    shuffled = random.sample(letters, len(letters))
    # Create our key
    key = {k: v for k, v in zip(letters, shuffled)}
    return key

def decode_key(keystring: str):
    # Decode our base64 string, then using pickle to load it.
    decoded = base64.urlsafe_b64decode(keystring)
    return pickle.loads(decoded)

def encode_key(key: Dict[str, str]):
    # Serialize our key to bytes using pickle, then encode the
    # bytes to base64 for easier copy/pasting.
    serialized = pickle.dumps(key)
    return base64.urlsafe_b64decode(serialized)