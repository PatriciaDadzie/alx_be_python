import datetime

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.datetime.now()

    # Format it to "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Display the result
    print("Current Date and Time:", formatted_date)

# Call the function
display_current_datetime()




def calculate_future_date():
    # Ask the user for a number of days
    days = int(input("Enter number of days from today: "))

    # Get today's date
    today = datetime.date.today()

    # Add the number of days to today's date
    future_date = today + datetime.timedelta(days=days)

    # Print the future date in "YYYY-MM-DD" format
    print("The date after", days, "days will be:", future_date.strftime("%Y-%m-%d"))

# Call the function
calculate_future_date()
