def brute_force_attack(password_list,target_password):
    for password in password_list:
        print(f"trying password:{password}")

        if password==target_password:
          print(f"password found:{password}")
          return True
        
    print("password not found")
    return False


if __name__=="__main__":
   password_list={
      "123456","password","123456789","12345678",
      "qwerty","abc123","monkey","letmein",
      "dragon","1111","baseball"
   }

   target_password=input("enter the target password:")
   print("starting brute force attack...")
   success=brute_force_attack(password_list,target_password)

   if success:
      print("brute force atttack successful!")

   else:
      print("brute force attack failed.")


      
    

