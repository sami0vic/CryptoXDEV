import hashlib
from termcolor import colored
import itertools

allowed_ids = [
    "XDEV-0000", "XDEV-0002", "XDEV-0013", "XDEV-0020", "XDEV-0025", "XDEV-0026", "XDEV-0027", "XDEV-0028", 
    "XDEV-0029", "XDEV-0030", "XDEV-0031", "XDEV-0032", "XDEV-0033", "XDEV-0034", "XDEV-0035", "XDEV-0036", 
    "XDEV-0037", "XDEV-0038", "XDEV-0039", "XDEV-0040", "XDEV-0041", "XDEV-0042", "XDEV-0043", "XDEV-0044", 
    "XDEV-0045", "XDEV-0119", "XDEV-0046", "XDEV-0047", "XDEV-0048", "XDEV-0049", "XDEV-0050", "XDEV-0051", 
    "XDEV-0052", "XDEV-0053", "XDEV-0054", "XDEV-0055", "XDEV-0056", "XDEV-0057", "XDEV-0058", "XDEV-0059", 
    "XDEV-0060", "XDEV-0061", "XDEV-0062", "XDEV-0063", "XDEV-0064", "XDEV-0065", "XDEV-0066", "XDEV-0067", 
    "XDEV-0068", "XDEV-0070", "XDEV-0071", "XDEV-0072", "XDEV-0073", "XDEV-0074", "XDEV-0075", "XDEV-0076", 
    "XDEV-0077", "XDEV-0078", "XDEV-0079", "XDEV-0080", "XDEV-0081", "XDEV-0082", "XDEV-0083", "XDEV-0084", 
    "XDEV-0085", "XDEV-0086", "XDEV-0087", "XDEV-0088", "XDEV-0089", "XDEV-0090", "XDEV-0091", "XDEV-0115", 
    "XDEV-0021", "XDEV-0069", "XDEV-0092", "XDEV-0093", "XDEV-0094", "XDEV-0095", "XDEV-0096", "XDEV-0097", 
    "XDEV-0098", "XDEV-0099", "XDEV-0100", "XDEV-0101", "XDEV-0102", "XDEV-0103", "XDEV-0104", "XDEV-0105", 
    "XDEV-0106", "XDEV-0107", "XDEV-0108", "XDEV-0109", "XDEV-0110", "XDEV-0111", "XDEV-0112", "XDEV-0113", 
    "XDEV-0114", "XDEV-0116", "XDEV-0117", "XDEV-0118"
]

def login():
    member_id = input("Enter your member ID (e.g., XDEV-3301): ")
    if member_id not in allowed_ids:
        print("Access denied. Your member ID is not authorized.")
        login()
    elif(member_id in allowed_ids):
        choose()

def crack_md5(target_hash):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    hash_length = len(target_hash)

    for password_length in range(0, 7):  # You can adjust the length of passwords to check
        for password in itertools.product(characters, repeat=password_length):
            candidate = "".join(password)
            candidate_hash = hashlib.md5(candidate.encode()).hexdigest()

            if candidate_hash == target_hash:
                return candidate

    return None

def choose():
    print("""
    1) Hash with MD5
    2) Crack the MD5 Hash
    """)
    choice = int(input("Enter your choice 1-2: "))
    match choice:
        case 1:
            plaintext = input("Please Enter a text to hash it with MD5: ")
            md5_hashed_text = hashlib.md5(plaintext.encode())
            print("The MD5 Hash of your text is:", md5_hashed_text.hexdigest())
            repeat()
        case 2:
            target_hash = input("Please Enter an MD5 hash to crack: ")
            cracked_text = crack_md5(target_hash)
            if cracked_text:
                print(f"The original text for the MD5 hash is: {cracked_text}")
            else:
                print("Failed to crack the MD5 hash.")
            repeat()
        case _:
            return

def repeat():
    WantToRepeat = input("Do you want to continue? [Y/n]")
    if(WantToRepeat == "Y"):
        choose()
    else:
        return


print(colored("""
H   H  EEEEE  L      L       O      X     X  DDDD   EEEEE  V       V
H   H  E      L      L      O O      X   X   D   D  E       V     V
HHHHH  EEEE   L      L     O   O       X     D   D  EEEE     V   V
H   H  E      L      L      O O      X   X   D   D  E         V V
H   H  EEEEE  LLLLL  LLLLL   O      X     X  DDDD   EEEEE      V
""", "green"))
login()
