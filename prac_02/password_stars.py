def main():
minimum_length = 10
password = input("Enter password: ")
while len(password) != minimum_length:
    password = input("Enter password: ")
print("*" * len(password))


main()