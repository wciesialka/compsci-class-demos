import subprocess
import re
import tempfile
from hashlib import md5
from pathlib import Path
from time import perf_counter
from getpass import getpass

my_path = Path(__file__)
hashcat_path = my_path.parent / Path(r"hashcat-6.2.6\hashcat.exe")

def run(args):
    try:
        process = subprocess.run(args, capture_output=True, check=True, cwd=hashcat_path.parent)
        return process.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"Command: {e.cmd}")
        print(f"Return code: {e.returncode}")
        print(f"Standard output: {e.stdout.decode('utf-8', errors='ignore')}")
        print(f"Standard error: {e.stderr.decode('utf-8', errors='ignore')}")
        return b''  # Return empty bytes on error, handle it in crack()

def passhash(password):
    hashed = md5(password.encode("utf-8"))
    return hashed.hexdigest()

def crack(h, mask, /, charset_1=None, charset_2=None, charset_3=None, charset_4=None):
    print("Cracking password...")
    args = [hashcat_path, "-a3", "-m0", "--potfile-disable", '--quiet', h, mask]
    if charset_1:
        args.append(f"-1{charset_1}")
    if charset_2:
        args.append(f"-2{charset_2}")
    if charset_3:
        args.append(f"-3{charset_3}")
    if charset_4:
        args.append(f"-4{charset_4}")
    sp = run(args)  # Get the output of the hashcat command
    if sp: # check if the command was successful
        print("Retrieving password...")
        msg = sp.decode().strip()
        value = msg.split(":")
        return sp.decode(), value
    else:
        return sp.decode(), None # return None if the command failed

def get_inputs():
    password = getpass("Password to crack: ")
    print("""
   ? | Charset
 ===+=========
  ?l | abcdefghijklmnopqrstuvwxyz [a-z]
  ?u | ABCDEFGHIJKLMNOPQRSTUVWXYZ [A-Z]
  ?d | 0123456789                 [0-9]
  ?h | 0123456789abcdef           [0-9a-f]
  ?H | 0123456789ABCDEF           [0-9A-F]
  ?s |  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  ?a | ?l?u?d?s
  ?b | 0x00 - 0xff
  """)
    mask = input("Cracking Mask: ")
    charsets = []
    for i in range(4):
        charset = input(f"Charset #{i+1} (Leave blank for none): ")
        if charset:
            charsets.append(charset)
            continue
        break
    return (password, mask, charsets)

def main():
    password, mask, charsets = get_inputs()
    h = passhash(password)
    print(f"Hashed password: {h}")
    
    start = perf_counter()
    progress, result = crack(h, mask, *charsets)
    end = perf_counter()

    cracked_hash, cracked_pass = result

    print(f"Cracked hash {cracked_hash} in {end-start:.2f}s. \nPassword: {cracked_pass}")

if __name__ == "__main__":
    main()
