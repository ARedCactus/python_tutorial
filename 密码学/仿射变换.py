def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def find_key(plain, cipher):
    i, f = ord('i') - ord('a'), ord('f') - ord('a')
    e, d = ord('e') - ord('a'), ord('d') - ord('a')

    for a in range(26):
        b = (e - a * i) % 26
        if (d - a * f) % 26 == b and gcd(a, 26) == 1:
            return a, b
    return None, None


def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            x = ord(char) - ord('a')
            p = (a_inv * (x - b)) % 26
            plaintext += chr(p + ord('a'))
        else:
            plaintext += char
    return plaintext


# 已知明文和密文对
known_plain = "if"
known_cipher = "ed"

a, b = find_key(known_plain, known_cipher)
print(a, b)

if a and b:
    ciphertext = "edsgickxhuklzveqzvkxwkzukvcuh"
    decrypted_text = affine_decrypt(ciphertext, a, b)
    print("Decrypted text:", decrypted_text)
else:
    print("Unable to find keys a and b")

