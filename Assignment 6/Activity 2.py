def calculate_Days(age):
    days = age * 365
    return days

def calculate_Hours(age):
    hours = age * 8760    
    return hours

def calculate_Months(age):
    months = age * 12    
    return months

def calculate_Seconds(age):
    seconds = age * 31536000    
    return seconds

def display_Result(months, days, hours, seconds):
    print(str(months) + " Months " + str(days) + " Days " + str(hours) + " Hours " + str(seconds) + " Seconds ")

def get_Age():
    print("Enter Age")
    age = int(input())    
    return age

# Main
# This program shows an expected age in months, days, hours, and seconds.
age = get_Age()
months = calculate_Months(age)
days = calculate_Days(age)
hours = calculate_Hours(age)
seconds = calculate_Seconds(age)
display_Result(months, days, hours, seconds)

# References: https://www.youtube.com/watch?v=FWaN3lTyhPU
