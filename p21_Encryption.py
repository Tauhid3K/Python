import random
import string

chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters

chars = list(chars) # Create a list of characters including space, whitespace, punctuation, digits, and letters
key = chars.copy()  # Create a copy of the chars list to use as the key
random.shuffle(key)

#print(f"Key: {key}")
#print(f"Chars: {chars}")

#Encryption

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:       # Get each letter from the plain text
    index = chars.index(letter) # Find the index of the letter in the chars list
    cipher_text += key[index]   # Append the corresponding letter from the key list to the cipher text

print()
print(f"Plain Text: {plain_text}")
print(f"Cipher Text: {cipher_text}")

#Decryption

print()
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:     # Get each letter from the cipher text
    index = key.index(letter)  # Find the index of the letter in the key list
    plain_text += chars[index] # Append the corresponding letter from the chars list to the plain text

print()
print(f"Cipher Text: {cipher_text}")
print(f"Plain Text: {plain_text}")