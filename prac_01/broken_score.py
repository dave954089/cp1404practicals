score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")  # for validating input
else:
    if score >= 90:
        print("Excellent")  # scoring
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
