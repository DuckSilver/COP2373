import re

def phone_num(phone):
    check = re.compile(r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    valid_phone = bool(check.match(phone))
    if valid_phone == True:
        print("This phone number is valid")
        print(" ")
    else:
        print("This phone number is invalid")
        print(" ")


def ssn(social):
    check = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    valid_social = bool(check.match(social))
    if valid_social == True:
        print("This SSN is valid")
        print(" ")
    else:
        print("This SSN is invalid")
        print(" ")

def zip_code(zip):
    check = re.compile(r'^\d{5}(-\d{4})?$')
    valid_zip = bool(check.match(zip))
    if valid_zip == True:
        print("This zip code is valid")
    else:
        print("This zip code is invalid")

def main():
    print("Please enter the following:")
    print("Format example: 123-456-7890")
    phone = input("Phone Number: ")
    print(" ")
    print("Format example: 123-45-6789")
    social = input("Social Security Number: ")
    print(" ")
    print("Format example: 12345 /or 12345-1234")
    zip = input("Zip code: ")
    print(" ")
    print(" ")

    phone_num(phone)
    ssn(social)
    zip_code(zip)

main()