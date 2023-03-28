"""
CP1404
email
"""


def main():
    email_to_name = {}
    email_address = input("Enter your email: ")
    while email_address != "":
        name = extract_name(email_address)
        prompt_check = input(f"Is your name {name} ?  (Y/N) ").upper()
        if prompt_check != "y" and prompt_check != " ":
            name = input("Enter your name: ")
        email_to_name[email_address] = name
        email_address = input("Enter your email: ")
    else:
        print("Thank you!")
    for email, name in email_to_name.items():
        print(f"{name} : {email}")


def extract_name(email_address):
    prefix = email_address.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
