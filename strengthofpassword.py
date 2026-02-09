import re

def password_strength(password):
    if len(password)<8:
        print("password id too short")
    
    elif not re.search("[a-z]",password):
        print("password should have at least one lowercase letter")

    elif not re.search("[0-9]",password):
        print("password should have atleast one digit")

    elif not re.search("[A-Z]",password):
        print("password should have atleast one uppercase letter")


    elif not re.search("[!@#$%^&*(),,?\":{}|<>]",password):
        print("password should have atleast one special character")

    else:
        print("password is strong")


user_password = input("enter a password to check its strength:")
password_strength(user_password)