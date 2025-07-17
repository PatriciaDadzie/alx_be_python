# Multiplication Table Generator

# Ask the user to input a number for which they want to see the multiplication table
number = int(input("Enter a number to see its multiplication table: "))

# iterate from i = 1 to i = 10
for i in range(1, 11):
    result = i * number 
    print(f"{number} * {i} = {result}")