import random

# Set the available characters for the password.
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['1', '2', '3', '4', '5', '6', '8', '9', '0']
special_characters_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']','^', '_', '`', '{', '}', '|', '~']

# Take input to what the password will look like.
length_of_password = int(input("How long do you want the password to be? "))
password_length = length_of_password

password_numbers_active = input("Do you want the password to have numbers? y/n ")
if password_numbers_active == "y":
    password_numbers_active = True
else:
    password_numbers_active = False

password_capital_letters_active = input("Do you want the password to have capital letters? y/n ")
if password_capital_letters_active == "y":
    password_capital_letters_active = True
else:
    password_capital_letters_active = False

# Check if the special character is one in the list.
password_special_characters_active = input("Do you want the password to include special characters? y/n ")
while True:
    if password_special_characters_active == "y":
        special_characters_active_list = [input("What special characters do you want?")]
        if any(item in special_characters_active_list for item in special_characters_list):
            password_special_characters_active = True
            break
        else:
            print(f"Your special character have to be one of these: {special_characters_list}")
    else:
        password_special_characters_active = "n"
        break

# A class that generates the password.
class Password_Generator():
    def __init__(self, length, numbers, capital_letters, special_characters):
        self.length = length
        self.numbers = numbers
        self.capital_letters = capital_letters
        self.special_characters = special_characters

        password = ""
        list_of_characters = []
        list_of_characters += lowercase_letters
        if self.numbers == True:
            list_of_characters += numbers_list
        else:
            pass
        if self.special_characters == True:
            list_of_characters += special_characters_active_list
        else:
            pass
        if self.capital_letters == True:
            list_of_characters += uppercase_letters
        else:
            pass
        for i in range(self.length):
            password += random.choice(list_of_characters)
        #print(list_of_characters)
        print("Your password is: " + password)

# Generate the password with everything the user wants in it.
Password_Generator(password_length, password_numbers_active, password_capital_letters_active, password_special_characters_active)
#print(length_of_password, password_numbers_active, password_capital_letters_active, password_special_characters_active)