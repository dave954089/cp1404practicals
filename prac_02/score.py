import random


def main():
    score = gettihg_score()
    result = scoring(score)
    print(result)


def gettihg_score():
    score = random.randint(0, 100)
    # score = float(input("Enter score: "))
    # while score < 0 or score > 100:
    #     print("Invalid score")  # for validating input
    #     score = gettihg_score()
    return score


def scoring(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
