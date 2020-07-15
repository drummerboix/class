# Password generator by ADEDAMOLA OGUNBONA

# import library for random stuff
from random import *
# for letters stuff
import string

# make pre-requisites
char1 = string.ascii_uppercase
char2 = char1.lower()
char3 = "0123456789"
char4 = "!@#$%^&*()"

# Welcome messages
def message():
    print("Hello man, let's get you a password")
    print("Please select the length of your password")
    print(userGen())

# User inputs for all 4 elements
def userGen():
    upper = int(input("Input number of upper case characters: "))
    lower = int(input("Input number of lower case characters: "))
    spec = int(input("Input number of special characters: "))
    num = int(input("Input number of integer characters: "))
    return passGen(upper,lower,spec,num)

# Generating passwords from random stuff
def passGen(upper,lower,spec,num):
    newpass = []
    if (upper+lower+spec+num)<6:
        print("Enter minimum 6 characters")
    else:
        for i in range(upper):
            newpass += choice(char1)
        for i in range(lower):
            newpass += choice(char2)
        for i in range(spec):
            newpass += choice(char4)
        for i in range(num):
            newpass += choice(char3)
    password = list(newpass)
    shuff = shuffle(password)
    acpass = "".join(password)
    return acpass
message()
