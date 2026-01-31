from datetime import datetime

def calculate_age(dob):
    # Get today's date
    today = datetime.today()
    
    # Calculate the difference in years, months, and days
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    # Adjust if the current day/month hasn't reached the birth day/month yet
    if days < 0:
        months -= 1
        days += (today - datetime(today.year, today.month - 1, dob.day)).days
    if months < 0:
        years -= 1
        months += 12

    # Calculate the total number of days alive
    total_days_alive = (today - dob).days
    
    return years, months, days, total_days_alive

# Input and validation
dob_input = input("Please enter your DOB (MM/DD/YYYY): ")

try:
    # Convert the input into a date object
    dob = datetime.strptime(dob_input, "%m/%d/%Y")
    
    # Calculate age
    years, months, days, total_days_alive = calculate_age(dob)

    # Output the result
    print(f"You are {years} years, {months} months, and {days} days old.")
    print(f"You have been alive for {total_days_alive} days.")

except ValueError:
    print("Invalid date format. Please use MM/DD/YYYY.")
