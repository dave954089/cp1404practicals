"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD ": "Queensland", "NSW": "New South Wales", "NT   ": "Northern Territory", "WA  ": "Western Australia ",
                "ACT ": "Australian Capital Territory", "VIC  ": "Victoria", "TAS ": "Tasmania"}

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    elif state_code == "ALL":  # To print all states in loop
        for state in CODE_TO_NAME:
            print(state, "  is  " ,CODE_TO_NAME[state])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()