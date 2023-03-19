def encrypt(plaintext, key):
    cipher_text = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            cipher_text[col] += plaintext[pointer]
            pointer += key
    return ''.join(cipher_text)

def decrypt(ciphertext, key):
    plain_text = [''] * (len(ciphertext) // key)
    for col in range(key):
        pointer = col
        for row in range(len(ciphertext) // key):
            plain_text[row] += ciphertext[pointer]
            pointer += key
    return ''.join(plain_text)

plaintext = "Fitrah Fajarianto"
key = 6
print(plaintext)
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
