def generate_key(plaintext, key):
    repeating_key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    return repeating_key

def encrypt(plaintext, key):
    ciphertext = ""
    repeating_key = generate_key(plaintext, key)
    for i in range(len(plaintext)):
        shift = ord(repeating_key[i]) - 65
        if plaintext[i].isupper():
            shifted_char = chr((ord(plaintext[i]) + shift - 65) % 26 + 65)
            ciphertext += shifted_char
        elif plaintext[i].islower():
            shifted_char = chr((ord(plaintext[i]) + shift - 97) % 26 + 97)
            ciphertext += shifted_char
        else:
            ciphertext += plaintext[i]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    repeating_key = generate_key(ciphertext, key)
    for i in range(len(ciphertext)):
        shift = ord(repeating_key[i]) - 65
        if ciphertext[i].isupper():
            shifted_char = chr((ord(ciphertext[i]) - shift - 65) % 26 + 65)
            plaintext += shifted_char
        elif ciphertext[i].islower():
            shifted_char = chr((ord(ciphertext[i]) - shift - 97) % 26 + 97)
            plaintext += shifted_char
        else:
            plaintext += ciphertext[i]
    return plaintext

plaintext = "SEMANGAT"
key = "261"
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
