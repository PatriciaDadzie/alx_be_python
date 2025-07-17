
# A simple match case calculator

# Take first and second numbers from user
num1 = float(input(" Enter the first number: "))
num2 = float(input(" Enter the second number: "))

# Ask user for preferred operation
operation = input(" Choose the operation (+, -, *, /): " )

# Match case
match operation :
    case "+":
        result = num1 + num2
        print(f"The result is: {result} ")

    case "-":
         result = num1 - num2
         print(f"The result is: {result} ")

    case "*":
         result = num1 * num2
         print(f"The result is: {result} ")

    case "/":
          if num2 == 0:
            print(" Cannot divide by zero.")

          else :
            result = num1 / num2
            print(f"The result is {result}.")
        