def cesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha(): 
            if char.isupper():
                encrypted_char = chr((ord(char)-ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char)-ord('a') + shift) % 26 + ord('a'))
            encrypted_text+=encrypted_char

        else:
            encrypted_text += char 

    return encrypted_text


 
text=input("enter the plaintext: ")
shift=int(input("enter the shift value: "))


encrypted_text = cesar_cipher_encrypt(text, shift)

print("encrypted text",encrypted_text)
