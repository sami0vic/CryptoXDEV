import hashlib
import termcolor
from termcolor import colored

print(colored("""
M   M  DDDD   5555      H   H    AAAAA  SSSS  H   H
MM MM  D   D  5         H   H    A   A  S     H   H
M M M  D   D  555       HHHHH    AAAAA  SSSS  HHHHH
M   M  D   D     5      H   H    A   A     S  H   H
M   M  DDDD   555       H   H    A   A  SSSS  H   H
""", "green"))

plaintext = input("Please Enter a text to hash it with MD5: ")
md5_hashed_text = hashlib.md5(plaintext.encode())
print("The MD5 Hash of your text is:", md5_hashed_text.hexdigest())
