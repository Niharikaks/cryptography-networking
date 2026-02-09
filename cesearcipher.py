def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26
            # Check if it's uppercase or lowercase
            if char.isupper():
                encrypted_text += chr((ord(char) + shift_amount - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift_amount - 97) % 26 + 97)
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text
# Function to decrypt the message
def decrypt(text, shift):
    return encrypt(text, -shift)  # Decrypt by shifting in the opposite direction
# Example usage
message = "Hello, World!"
shift_value = 3
# Encrypting the message
encrypted_message = encrypt(message, shift_value)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
# Decrypting the message
decrypted_message = decrypt(encrypted_message, shift_value)
print(f"Decrypted Message: {decrypted_message}")
