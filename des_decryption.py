#!/usr/bin/env python3
    

CIPHERTEXT = 1100101011101101101000100110010101011111101101110011100001110011

# tables

pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

left_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
ip = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
ip1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

# expansion table
E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# s-boxes
sboxes = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

# p table
p = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

def permute(key, table):
    # apply pc-1
    new_key = []
    for i in table:
        new_key.append(key[i-1])
    return ''.join(map(str, new_key))

def permute2(c, d):

    key = c + d
    new_key = []
    for i in pc2:
        new_key.append(key[i-1])
    return ''.join(map(str, new_key))

def shift_left(key, n):
    # n = n % len(key)
    return key[n:] + key[:n]


def generate_keys(key):
    # apply pc-1
    # key is a string
    key = permute(key, pc1)
    print(f'PC-1 Permutation: {key}')

    c0 = key[:28]
    d0 = key[28:]

    print(f'C0: {c0}')
    print(f'D0: {d0}')

    c = []
    d = []

    left = c0
    right = d0
    for i in range(0, 16):
        left = shift_left(left, left_shifts[i])
        right = shift_left(right, left_shifts[i])
        c.append(left)
        d.append(right)

    print('Keys after left shifts:')
    for i in range(16):
        print(f'C{i+1}: {c[i]} | D{i+1}: {d[i]}')

    
    # apply pc-2
    round_keys = []
    for i in range(16):
        ki = permute2(c[i], d[i])
        round_keys.append(ki)

    # reverse order of the round keys
    round_keys = round_keys[::-1]
    
    return round_keys    

def xor(bits, key):
    bits = [int(bit) for bit in bits]
    key = [int(bit) for bit in key]
    result = []
    for i in range(len(bits)):
        result.append(bits[i] ^ key[i])
    return ''.join(map(str, result))

def apply_sboxes(bits):
    s_result = ''
    for i in range(0, len(bits), 6):
        middle = bits[i:i+6]
        r = int(str(middle[0]) + str(middle[5]), 2)
        c = int(''.join(map(str, middle[1:5])), 2)
        
        num = sboxes[i//6][r][c]
        num = format(num, '04b')
        s_result += num
        
    print(f'S-BOX: {s_result}')
    return s_result

def apply_p(sbox_result):
    p_result = ''
    for i in p:
        p_result += sbox_result[i-1]
    return p_result
    

def decrypt(ciphertext, round_keys):
    bits = permute(ciphertext, ip)
    print(f'Initial permutation of ciphertext: {bits}')

    l0 = bits[:32]
    r0 = bits[32:]


    print(f'L0: {l0} | R0: {r0}') 

    for i in range(16):
        print(f'Round {i+1}')
        print('-----------------')
        # expand r0
        r0_exp = permute(r0, E) # this r0 is definitely right
        print(f'R0 expanded: {r0_exp}')
        xor_result = xor(r0_exp, round_keys[i])
        xor_result = ''.join(map(str, xor_result))

        print(f'XOR with key: {xor_result}')

        # apply s-boxes
        sbox_result = apply_sboxes(xor_result)
        print(f'After S-BOX: {sbox_result}')

        # apply p
        p_result = apply_p(sbox_result)
        print(f'After P-BOX: {p_result}')
        
        # xor with l0
        xor_result2 = xor(p_result, l0)
        print(f'XOR with L0: {xor_result2}')

        
    # switch l0 and r0
        l0 = ''.join(map(str, r0))
        r0 = xor_result2

    combined = r0 + l0
    combined = ''.join(map(str, combined))
    print(f'\nAfter 16, rounds, swapping L & R: {combined}')
    # apply ip-1
    result = permute(combined, ip1)
    print(f'Apply IP-1: {result}')
    return result

def bin_to_text(binary):

    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        text += chr(int(byte, 2))

    return text


def main():
    K = '0100110001001111010101100100010101000011010100110100111001000100'
    CIPHERTEXT = '1100101011101101101000100110010101011111101101110011100001110011'   

    print(f'Key: {K}')
    print(f'Ciphertext: {CIPHERTEXT}')

    round_keys = generate_keys(K)
    print(f'Round Keys')
    for i, key in enumerate(round_keys):
        print(f'Key {i+1}: {key}')


    decrypted = decrypt(CIPHERTEXT, round_keys)
    text = bin_to_text(decrypted)
    print(f'Decrypted text: {text}')



if __name__ == "__main__":
    main()