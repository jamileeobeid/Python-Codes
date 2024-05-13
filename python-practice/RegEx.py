import re

def find_digits(a_str):

    for match in re.findall("[0-9]+", a_str):
        print(match, end=' ')

find_digits("01ab02cd03ef")  #01 02 03

print("\n")


def find_digits(a_str):

    for match in re.findall("\D\D", a_str):
        print(match, end=' ')

find_digits("01ab02cd03ef") #ab cd ef

print("\n")


def find_digits(a_str):

    for match in re.findall("\D+", a_str):
        print(match, end=' ')

find_digits("01ab02cd03ef") #ab cd ef

print("\n")


def find_digits(a_str):

    for match in re.findall("\D{1}", a_str):
        print(match, end=' ')

find_digits("HE01LL02O03")

print("\n")


#checking if the value at each index of the string whether they're a digit or not

def isornotdigit(message):

    for i in message:

        if i.isdigit():
            print(i, "is a digit")

        if not i.isdigit():
            print(i, "is not a digit")

isornotdigit("hey123@hello99")


#appending @ in the spaces in the string

def isornotspace(message):

    for i in message:

        if i.isspace():
            print("@")

        if not i.isspace():
            print(i)

isornotspace("ex mpl e")