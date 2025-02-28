#!/usr/bin/env python3

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
STATISTICS = {'A': 0.08, 'B': 0.015, 'C': 0.03, 
              'D': 0.04, 'E': 0.13, 'F': 0.02, 
              'G': 0.015, 'H': 0.06, 'I': 0.065, 
              'J': 0.005, 'K': 0.005, 'L': 0.035, 
              'M': 0.03, 'N': 0.07, 'O': 0.08, 
              'P': 0.02, 'Q': 0.002, 'R': 0.065, 
              'S': 0.06, 'T': 0.09, 'U': 0.03, 
              'V': 0.01, 'W': 0.015, 'X': 0.005,
              'Y': 0.02, 'Z': 0.002}

def compute_frequencies(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
        
    for key in frequency:
        frequency[key] = frequency[key] / len(text)
    
    return frequency


def phi(text, frequencies):
    s = 0
    phi_vals = {}
    # get frequency of letter in the text and then also statistics of that letter shifted by shift
    for i in range(26):
        s = 0
        for char in set(text):
            shifted_char = ALPHABET[(ALPHABET.index(char) - i) % 26]
            s += frequencies[char] * STATISTICS[shifted_char]
        phi_vals[i] = s


    for key in phi_vals:
        print(f'{key}: {phi_vals[key]:.5f}')
    return phi_vals
        
    

def shift(text):
    s = 7
    shifted_text = ""
    for char in text:
        shifted_text += ALPHABET[(ALPHABET.index(char) - s) % 26]
    return shifted_text

def main():
    text = "JVTWBALYZJPLUJL"
    frequencies = compute_frequencies(text)
    phi_vals = phi(text, frequencies)

    print(shift(text))


if __name__ == "__main__":
    main()