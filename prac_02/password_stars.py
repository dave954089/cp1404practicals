def main():
    minimum_length = 10
    password = get_password()
    while len(password) != minimum_length:
        get_password()
    print_stars(password)


def get_password():
    password = input("Enter password: ")
    return password


def print_stars(password):
    print("*" * len(password))


main()
