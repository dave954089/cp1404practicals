def main():
    choice = choice_selection()
    while choice != "Q":  # To select choices in menu
        if choice == "G":
            score = gettihg_score()
        elif choice == "P":
            score = gettihg_score()
        elif choice == "S":
            print_star(score)
        else:
            print("Invalid choice")
        choice = choice_selection()
    print("Farewell")


def choice_selection():
    print("(G)et a valid score  \n(P)rint result \nS)how stars \n(Q)uit)")
    choice = input(">>> ").upper()
    return choice


def gettihg_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")  # for validating input
        score = gettihg_score()
    return score


def print_star(score):
    print("*" * score)


def score_result(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    print(result)


main()
