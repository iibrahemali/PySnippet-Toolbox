import random
import string 

def generate_password(min_len, num, special_char):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if num:
        characters += digits
    if special_char:
        characters += special

    pwd = ""
    criteria = False
    has_number = False
    has_special = False

    while not criteria or len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True 

        criteria = True
        if num:
            criteria = criteria and has_number
        if special_char:
            criteria = criteria and has_special

    return pwd

def main():
    min_len = int(input("Give me the minimum length!\n -->"))
    print("Set your Criteria")
    print("________________________________________________")
    has_number = input("Do you want numbers? (y/n)").lower() == "y"
    has_special = input("Do you want special characters? (y/n)").lower() == "y"
    password = generate_password(min_len, has_number, has_special)
    print("The password is: " + password)

if __name__ == "__main__":
    main()



#########        
    #
    #
    #
    #
    #
    #
#########
    