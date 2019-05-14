# Caesar Cipher
# Each letter replaced by a letter with 'shift' positions down the alphabet.


def encrypt(text, s):
    encrypted_txt = ""
    for c in text:
        if c == ' ':
            encrypted_txt += ' '
        elif c.isupper():
            new_pos = (ord(c) - 65 + s) % 26 + 65
            encrypted_txt += chr(new_pos)
        else:
            new_pos = (ord(c) - 97 + s) % 26 + 97
            encrypted_txt += chr(new_pos)
    return encrypted_txt


def decrypt(text, s):
    decrypted_txt = ""
    for c in text:
        if c == ' ':
            decrypted_txt += ' '
        elif c.isupper():
            new_pos = (ord(c) - 65 - s) % 26 + 65
            decrypted_txt += chr(new_pos)
        else:
            new_pos = (ord(c) - 97 - s) % 26 + 97
            decrypted_txt += chr(new_pos)
    return decrypted_txt
