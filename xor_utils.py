from keras.models import load_model
import numpy as np


def find_closest_prob(n: int):
    if 1 - n > n - 0:
        return 0
    else:
        return 1


def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length / len(string_to_expand)) + 1))[:length]


def encrypt(to_encrypt: str, key: str):
    bitstring = to_bits(to_encrypt)
    model = load_model('./model/xor.h5')
    key = to_bits(key)
    key = repeat_to_length(key, len(bitstring))

    # print(from_bits(key), "\n")

    encrypted_bits = []

    for i in range(len(bitstring)):
        encrypted_bits.append(find_closest_prob(model.predict_proba(np.array([[float(bitstring[i]), float(key[i])]]))))

    return from_bits(encrypted_bits), from_bits(key)


def decrypt(to_decrypt: str, key: str):
    bitstring = to_bits(to_decrypt)
    model = load_model('./model/xor.h5')
    key = to_bits(key)

    decrypted_bits = []

    for i in range(len(bitstring)):
        decrypted_bits.append(find_closest_prob(model.predict_proba(np.array([[float(bitstring[i]), float(key[i])]]))))

    return from_bits(decrypted_bits)


def to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def from_bits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)
