# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function that converts temp from Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    temp_in_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp_in_celsius

# Function that converts temp from Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    temp_in_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temp_in_fahrenheit

# Prompt user for temperature and unit, and handle wrong input
def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
          

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if unit.upper() == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        
        elif unit.upper() == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")

        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError as e:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
