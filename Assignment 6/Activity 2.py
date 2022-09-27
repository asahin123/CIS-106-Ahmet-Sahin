# Main
# This program shows an expected age in months, days, hours, and seconds.

# References: https://www.youtube.com/watch?v=FWaN3lTyhPU


def calculate_days(age):
    days = age * 365
    return days


def calculate_hours(age):
    hours = age * 8760    
    return hours


def calculate_months(age):
    months = age * 12    
    return months


def calculate_seconds(age):
    seconds = age * 31536000    
    return seconds


def display_result(months, days, hours, seconds):
    print(str(months) + " Months " + str(days) + " Days " + str(hours) 
         \ + " Hours " + str(seconds) + " Seconds ")
    

def get_age():
    print("Enter Age")
    age = int(input())    
    return age


def main():
    age = get_age()
    months = calculate_months(age)
    days = calculate_days(age)
    hours = calculate_hours(age)
    seconds = calculate_seconds(age)
    display_result(months, days, hours, seconds)
    

main()
