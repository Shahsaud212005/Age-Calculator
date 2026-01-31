import datetime
def days_counting(a, b):
    months = 30
    years = 365
    year_days = years * a
    month_days = months * b
    result = year_days + month_days + 6
    return result
    
today = str(datetime.date.today())
today_1 = today.replace("-", " ")
today_2 = today_1.split()

current_month = int(today_2[1])
current_day = int(today_2[2])
current_year = int(today_2[0])

dob = input("please enter your DOB in numbers (month/day/year): ")

if len(dob) > 10:
    input("please enter a valid DOB (e.g., 7/22/2005): ")

new_dob = dob.replace("/", " ")

new_dob_2 = new_dob.split()

month = int(new_dob_2[0])
day = int(new_dob_2[1])
year = int(new_dob_2[2])


result_1 = current_month - month
result_2 = current_day - day
result_3 = current_year - year

result = days_counting(result_3, result_1) + result_2

print(f"you are {result_3} years, {result_1} months and {result_2} days old.")
print(f"you are {result} days old")
