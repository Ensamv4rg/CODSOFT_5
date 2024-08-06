import random
import secrets
import string

def generatePassword(lenght,nums,special_chars,uppercase,lowercase,duplicates=True):
    #function arguments. Takes the minimum values for a string type.
    #variables
        #variables containing charachters for specific data type
    upper,lower,wildcards,numbers = string.ascii_uppercase,string.ascii_lowercase,string.punctuation,string.digits
        #variables for the characters,type and thier total values
    data_type = {'UCletter':uppercase,'LCletter':lowercase,'Symbol':special_chars,'digit':nums}
    if sum(data_type.values()):
        print("Warning, Length is longer than required calculations, Might result in unpredictable behaviour")
    data_map = {'UCletter':upper,'LCletter':lower,'Symbol':wildcards,'digit':numbers}
        #password
    password = ''

    while lenght:#runs till it has reached the required lenght
        add = random.choice(list(data_type))#selects a random charachter type
        if data_type[add] == 0 and sum(data_type.values()) != 0:#Code to select a new charcater if minimum requirements have been met for target type but other charcater requirements are not yet met
            continue
    
        chr = random.choice(data_map[add])#selects a random charachter based off the character type
        if not duplicates:#removes characther from source pool if it is already in the password(if duplicates are not allowed)
            data_map[add] = data_map[add].replace(chr,"")
        password +=chr#appends character to password
        if data_type[add] >=1:#reduces the number of minimum requirements by 1
            data_type[add] -= 1
        lenght -= 1

    return password#prints password
