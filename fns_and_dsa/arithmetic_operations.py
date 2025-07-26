
# Declaration of a function that performs basic arithmetic


def perform_operation(num1 , num2 , operation):

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