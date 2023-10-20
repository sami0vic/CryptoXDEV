from termcolor import colored
from time import sleep
def decrypt():
    
    # Enter your encrypted message(string) below
    encrypted_message = input("Enter the message to be decrypted: ").strip()
    
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Enter the key value to decrypt
    k = int(input("Enter the key to decrypt: "))
    decrypted_message = ""

    for ch in encrypted_message:
        if ch in letters:
            if ch.islower():
                position = letters.find(ch)
                new_pos = (position - k) % 26
                new_char = letters[new_pos]
            else:
                position = letters.find(ch)
                new_pos = (position - k) % 26
                new_char = letters[new_pos + 26]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    print("\nDecrypting your message...\n")
    sleep(2)
    print("Stand by, almost finished...\n")
    sleep(2)
    print("Your decrypted message is: ", decrypted_message, end="\n")
    repeat()

def encrypt():
    
    # Enter your plaintext message(string) below
    plaintext_message = input("Enter the message to be encrypted: ").strip()
    
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Enter the key value to encrypt
    k = int(input("Enter the key to encrypt: "))
    encrypted_message = ""
    print("\nEcrypting your message...\n")
    sleep(2)
    print("Stand by, almost finished...\n")
    sleep(2)

    for ch in plaintext_message:
        if ch in letters:
            if ch.islower():
                position = letters.find(ch)
                new_pos = (position + k) % 26
                new_char = letters[new_pos]
            else:
                position = letters.find(ch)
                new_pos = (position + k) % 26
                new_char = letters[new_pos - 26]
            encrypted_message += new_char
        else:
            encrypted_message += ch
    print("Your encrypted message is: ", encrypted_message, end="\n")
    repeat()

def bruteforce():
    
    # Enter your encrypted message(string) below
    encrypted_message = input("Enter the message to be brute forced: ").strip()

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("\nBrute Forcing your message...\n")
    sleep(2)
    print("Stand by, almost finished...\n")
    sleep(2)
    for key in range(len(letters)):
        translated = ''
        for ch in encrypted_message:
            if ch in letters:
                if ch.islower():
                    num = letters.find(ch.upper())  # Convert to uppercase for consistency
                    num = num - key
                    if num < 0:
                        num = num + len(letters)
                    translated = translated + letters[num].lower()  # Convert back to lowercase
                else:
                    num = letters.find(ch)
                    num = num - key
                    if num < 0:
                        num = num + len(letters)
                    translated = translated + letters[num]
            else:
                translated = translated + ch
        print(f'Hacking key is {key}: {translated}')
    repeat()

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

def choose():
    print("""
    1) Decrypt Caesar
    2) Encrypt with Caesar
    3) Brute Force Caesar
    """)
    choice = int(input("Enter your choice 1-3: "))
    match choice:
        case 1:
            decrypt()
        case 2:
            encrypt()
        case 3:
            bruteforce()
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
