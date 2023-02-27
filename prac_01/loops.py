for i in range(1, 21, 2):
    print(i, end=' ')
print()
# a.
for i in range(0, 110, 10):  # To print 10s
    print(i, end=' ')
print()
# b.
for i in range(20, 0, -1):  # To print in reverse
    print(i, end=' ')
print()
# c.
number_of_stars = int(input("Number of stars: "))  # To print number of stars
for i in range(number_of_stars):
    print("*", end=" ")
print()
# d.
for i in range(number_of_stars):  # To print in patterns
    print("*" * 1)
