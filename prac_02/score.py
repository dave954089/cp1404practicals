import random


def main():
    score = getting_score()
    result = scoring(score)
    print(result)


def getting_score():
    score = random.randint(0, 100)
    # score = float(input("Enter score: "))
    # while score < 0 or score > 100:
    #     print("Invalid score")  # for validating input
    #     score = getting_score()
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
