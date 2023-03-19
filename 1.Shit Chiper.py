def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isdigit():
            shifted_char = str((int(char) + key) % 10)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isdigit():
            shifted_char = str((int(char) - key) % 10)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext

plaintext = "261"
key = 1
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
