from colorama import Fore, Style, init
import time

# Initialize colorama
init(autoreset=True)

# ==========================
# Banner
# ==========================

def banner():
    print(Fore.GREEN + r"""
██████╗  █████╗ ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
██║  ██║███████║██████╔╝█████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗
██████╔╝██║  ██║██║  ██║██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

      DARKCIPHER v1.0
  Secure Encryption Utility
""")

# ==========================
# Caesar Cipher Encrypt
# ==========================

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)

            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            result += char

    return result

# ==========================
# Caesar Cipher Decrypt
# ==========================

def decrypt(text, shift):
    return encrypt(text, -shift)

# ==========================
# Main Menu
# ==========================

while True:

    banner()

    print(Fore.CYAN + "[1] Encrypt Message")
    print(Fore.CYAN + "[2] Decrypt Message")
    print(Fore.CYAN + "[3] Exit")

    choice = input(Fore.YELLOW + "\nroot@kali:~# ")

    # Encrypt
    if choice == "1":

        message = input(
            Fore.WHITE + "\nEnter Message: "
        )

        shift = int(
            input(Fore.WHITE + "Enter Shift Key (1-25): ")
        )

        print(Fore.BLUE + "\n[*] Encrypting Payload...")
        time.sleep(1)

        encrypted = encrypt(message, shift)

        print(
            Fore.GREEN +
            "\n[+] Encryption Successful!"
        )

        print(
            Fore.MAGENTA +
            "\nEncrypted Payload:"
        )

        print(Fore.WHITE + encrypted)

        input(
            Fore.YELLOW +
            "\nPress Enter to continue..."
        )

    # Decrypt
    elif choice == "2":

        ciphertext = input(
            Fore.WHITE +
            "\nEnter Ciphertext: "
        )

        shift = int(
            input(
                Fore.WHITE +
                "Enter Shift Key (1-25): "
            )
        )

        print(Fore.BLUE + "\n[*] Recovering Message...")
        time.sleep(1)

        decrypted = decrypt(ciphertext, shift)

        print(
            Fore.GREEN +
            "\n[+] Decryption Successful!"
        )

        print(
            Fore.MAGENTA +
            "\nRecovered Message:"
        )

        print(Fore.WHITE + decrypted)

        input(
            Fore.YELLOW +
            "\nPress Enter to continue..."
        )

    # Exit
    elif choice == "3":

        print(
            Fore.RED +
            "\n[!] Exiting DarkCipher..."
        )

        break

    else:

        print(
            Fore.RED +
            "\n[-] Invalid Option!"
        )

        time.sleep(1)
