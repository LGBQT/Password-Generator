import random

print("Hello! Let's generate a password")

### Define a list of characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!$%^&*"

### Prompt the user
passwordLength = int(input("How long would you like your password to be?"))

### Generate a random password
newPassword = [] 
for x in range(passwordLength):
    ### Append a random character to the password string
    newPassword.append(random.choice(characters))

    ### Join the whole list back into a string
    finalPassword = ''.join(map(str, newPassword))

    ### Let the user know their new password
    print("This is your new password: ", finalPassword)
  

