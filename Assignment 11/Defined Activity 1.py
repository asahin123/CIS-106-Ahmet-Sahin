# This program asks the user to enter a year and month number and then
# look up the corresponding month name and number of days and display
# the information. Continue accepting input until the user enters an
# invalid year or invalid month number.

# References: https://youtu.be/YPoxpgkftPI


def check_leap_year(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        february = 29
    else:
        february = 28

    return february


def display_finish():
    print("Program is stopped successfully")
    

def display_info(value):
    print("Please enter a valid " + value + " :")
    

def display_results(day, month, year):
    print(str(month) + str(year) + " has " + str(day) + " days.")
    

def get_month_days(year, value_month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days[1] = check_leap_year(year)

    month_days = days[value_month - 1]    
    return month_days


def get_month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]

    month_name = months[month_number - 1]    
    return month_name


def get_month():
    display_info("Month")
    month = int(input())
    return month


def get_year():
    display_info("Year")
    year = int(input())    
    return year


def main():
    while True:    
        year = get_year()
        if year < 1:
            break

        month = get_month()
        if month < 1 or month > 12:
            break

        day = get_month_days(year, month)
        month = get_month_name(month)
        display_results(day, month, year)

    display_finish()


main()
