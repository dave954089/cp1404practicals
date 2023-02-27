name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":  # To select choices in menu
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>> ").upper()
print("Finished.")