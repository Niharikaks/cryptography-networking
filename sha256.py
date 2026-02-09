import hashlib

def hash_string(text):
    hasher=hashlib.sha256()
    hasher.update(text.encode())
    return hasher.hexdigest()
 


text=input("enter any string")
hash_value=hash_string(text)

print("original text:",text)
print("SHA-256 hash:",hash_value)