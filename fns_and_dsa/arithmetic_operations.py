
# Declaration of a function that performs basic arithmetic
# (This funvtion would be called in a main.py script to perform operations defined)

def perform_operation(num1 , num2 , operation):

    # Match case to handle all the operations
    match operation:
        case "add":
            return num1 + num2

        case "subtract":
            return num1 - num2    

        case "multiply":
            return num1 * num2

        
        case "divide": 
         # If else to handle num2 = 0
         if num2 != 0:
            return num1 / num2
           
         else:
           return "Cannot divide by zero."