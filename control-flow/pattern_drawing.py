# Drawing Patterns with Nested Loops

# Ask the user to input a positive integer that represents the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Row counter
row = 0

# while loop to iterate through rows
while row < size:

     # Use a for loop to print asterisks in a row
    for i in range(size):
        print("*", end="")

    # Move to the next line after each row
    print()
    row += 1
