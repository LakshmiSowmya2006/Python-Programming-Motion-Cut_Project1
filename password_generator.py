import random

#Random module provides functions generating randomly

uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
special_chars="@#$%^!&*"

def generate_password(length):

 #Generates a random password with the specified length.

  all_characters = uppercase+lowercase+numbers+special_chars
  password = ""
  for _ in range(length):
      password += random.choice(all_characters)
      #Generates a password with random characters
  return password

if __name__ == "__main__":
    while True:
        try:
            length =int(input("Entire desired password length (e.g, 8,12,16):"))
            #User can get a paasword with a desired length
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    password = generate_password(length)
    print(f"Your generated password is: {password}")
    
