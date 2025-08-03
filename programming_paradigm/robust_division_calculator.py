# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Try performing the division
        result = num / denom
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values."
