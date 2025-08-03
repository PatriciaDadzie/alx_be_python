# robust_division_calculator.py


def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats 
        num = float(numerator)
        denom = float(denominator)

        result = num / denom
        return f"Result: {result}"
    
       #An exception to handle Zero Division error
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
        # An exception to handle Value error
    except ValueError:
        return "Error: Please enter numeric values only."
