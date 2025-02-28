#!/usr/bin/env python3

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def vigenere(text, key):

    index = 0
    cipher = ""
    while index < len(text):
        if index >= len(text):
            break
        letter = key[index % len(key)]
        cipher += ALPHABET[(ALPHABET.index(text[index]) + ALPHABET.index(letter)) % 26]
        index += 1
    return cipher


def main():
    text = "cryptographicprotocolsprovideacornerstoneforsecurecommunication"
    key = "und"
    print(vigenere(text, key))
    

if __name__ == "__main__":
    main()