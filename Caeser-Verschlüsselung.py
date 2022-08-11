wellcomming = input(
    "Hello there! this is the Caeser encryption-decryption system, do you want to encrypt or decrypt a text? ")
if wellcomming == "encrypt":
    plain_text = input("input the text you want it to be encrypted ").lower()
    shift = input("input the encryption key ")
    shift = int(shift) % 29
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(str(alphabet), str(shifted_alphabet))
    encrypted_text = plain_text.translate(table)
    print(encrypted_text)
elif wellcomming == "decrypt":
    encrypted_text = input(
        "input the text you want it to be decrypted ").lower()
    shift = input("input the encryption key ")
    shift = (int(shift) % 29) - (((int(shift) % 29)*2))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(str(alphabet), str(shifted_alphabet))
    decrypted_text = encrypted_text.translate(table)
    print(decrypted_text)
else:
    print("please rerun the programm and type encrpyt or decrypt properly")
