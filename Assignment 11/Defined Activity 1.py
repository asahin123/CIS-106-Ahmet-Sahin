# This program asks the user to enter a year and month number and then look up the:
# corresponding month name and number of days and display the information:
# Continue accepting input until the user enters an invalid year or invalid month number.

# References: https://youtu.be/YPoxpgkftPI

def check_leap_year(value_year):
    remainder = value_year % 100
    if remainder == 0:
        remainder = value_year % 400
        if remainder == 0:
            february = 29
        else:
            february = 28
    else:
        remainder = value_year % 4
        if remainder == 0:
            february = 29
        else:
            february = 28    
    return february


def display_finish():
    print("Program is stopped successfully")
    

def display_info(value):
    print("Please enter a valid " + value + " :")
    

def display_results(day, month, value_year):
    print(str(month) + str(value_year) + " has " + str(day) + " days.")
    

def get_month_days(value_year, value_month):
    days = [0] * (12)
    
    days[0] = 31
    days[1] = check_leap_year(value_year)
    days[2] = 31
    days[3] = 30
    days[4] = 31
    days[5] = 30
    days[6] = 31
    days[7] = 31
    days[8] = 30
    days[9] = 31
    days[10] = 30
    days[11] = 31
    month_days = days[value_month - 1]
    
    return month_days


def get_month_name(month_number):
    months = [""] * (12)
    
    months[0] = "January"
    months[1] = "February"
    months[2] = "March"
    months[3] = "April"
    months[4] = "May"
    months[5] = "June"
    months[6] = "July"
    months[7] = "August"
    months[8] = "September"
    months[9] = "October"
    months[10] = "November"
    months[11] = "December"
    month_name = months[month_number - 1]
    
    return month_name


def get_months():
    display_info("Month")
    month = int(input())
    
    return month


def get_years():
    display_info("Year")
    year = int(input())
    
    return year


def main():
    while True:    
        value_year = get_years()
        if value_year >= 1:
            value_month = get_months()
        if value_month >= 1 and value_month <= 12:
            day = get_month_days(value_year, value_month)
            month = get_month_name(value_month)
            display_results(day, month, value_year)
        else:
            display_finish()    
    else:
        display_finish()
    if not(value_year > 0 && value_month >= 1 && value_month <= 12)
main()
