def main():
    name = input("Enter name: ")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = choice_selection()
    while choice != "Q":  # To select choices in menu
        if choice == "H":
            print("Hello", name)
        elif choice == "G":
            print("Goodbye", name)
        else:
            print("Invalid choice")
        print("(H)ello\n(G)oodbye\n(Q)uit")
        choice = choice_selection()
    print("Finished.")


def choice_selection():
    choice = input(">>> ").upper()
    return choice


main()
