"""This module used both for encryption and decryption"""

from string import ascii_letters, digits
from math import fmod

text_url = "data/text.txt"
cipher_url = "data/cipher.txt"
open_text_url = "data/open_text.txt"
alphabet = list(ascii_letters + digits) + [".", ",", "!", "?", ";", "-", ":", "_"]


class Dictionary:
    """Dictionary class for getting symbol by specified key"""

    def __init__(self, key):
        self.key = key

    def get_symbol(self, old):
        index = alphabet.index(old) + self.key
        if abs(index) < len(alphabet):
            return alphabet[index]
        elif index > 0:
            return alphabet[index - len(alphabet)]


def read_file(file):
    with open(file) as f:
        text = ""
        for line in f.readlines():
            text += line
    return text


def write_file(file, text: str):
    with open(file, "w+") as f:
        f.writelines(text.splitlines(keepends=True))


def crypt(text, key):
    encrypted_text = ""
    dic = Dictionary(key)
    for letter in text:
        if letter in alphabet:
            encrypted_text += dic.get_symbol(letter)
        else:
            encrypted_text += letter
    return encrypted_text


def encrypt(key):
    encrypted_text = crypt(read_file(text_url), key)
    write_file(cipher_url, encrypted_text)
    print("Successfully encrypted")


if __name__ == '__main__':
    len(alphabet)
    encrypt(int(fmod(int(input("Input key: ")), len(alphabet))))
