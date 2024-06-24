import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

characters = list(uppercase + lowercase + digits + punctuation)

def generate_password(length: int = 12) -> int:
    random.shuffle(characters) #shuffle the original character list
    
    password = [random.choice(uppercase),
                random.choice(lowercase),
                random.choice(digits),
                random.choice(punctuation)]
    
    for i in range(length-4):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = ''.join(password)
    print("New Password:", password)

while True:
    option = input("Do you want to generate strong password? (Y/N): ").upper()
    if option == "Y":
        generate_password()
        break
    elif option == "N":
        break
    else:
        print("Invalid input, pls try again!!")
