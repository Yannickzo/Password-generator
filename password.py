import string
import random

#characters to generate password 

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()" )

def generate_random_password():

    #length of password
    length = 4
    #number of character types
    alphabets_count = 2
    digits_count = 1
    special_characters_count = 1
    
    characters_count = alphabets_count + digits_count + special_characters_count

    #check the total length with characters sum count
    #print not valid if the sum is greater than length
    if characters_count > length :
        print("characters total count is greater than the password length")
        return
    #initializing the password
    password = []
    #picking ramdom alphabets
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    #picking random digits
    for i in range(digits_count):
        password.append(random.choice(digits))

    #picking random special_characters
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))


    #shuffling the resultant passsword
    random.shuffle(password)

    #converting the list to string
    #printing the list
    print("" .join(password))

    #invoking the function
generate_random_password()