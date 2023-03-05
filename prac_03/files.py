""""
CP1402
"""

# 1.
input_file = open("name.txt", "w")
name=input("Enter your name: ")
print(name, file = input_file)
input_file.close()

# 2.
output_file = open("name.txt", "r")
output_file.read()
print("Your name is ", name)
output_file.close()

# 3.
output_file = open("numbers.txt", "r")
numb1 = int(output_file.readline())
numb2 = int(output_file.readline())
output_file.close()
print(numb1 + numb2)

# 4.
output_file = open("numbers.txt", "r")
total = 0
for line in output_file:
    number = int(line)
    total += number
output_file.close()
print("Total = ",total)