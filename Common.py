def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_primitive_root(q):
    for i in range(2, q):
        if len({pow(i, j, q) for j in range(1, q)}) == q - 1:
            return i

def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - base + shift % 26) % 26 + base)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = 26 - shift % 26
            base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            plaintext += char
    return plaintext
