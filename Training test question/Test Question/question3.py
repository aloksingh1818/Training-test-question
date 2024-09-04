import random
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

while True:
    
    password = generate_password()

    
    print(f"Generated password: {password}")
    
    
    choice = input("Do you like this password? (yes/no): ").strip().lower()
    
    if choice == 'yes':
        print(f"Your chosen password is: {password}")
        break
