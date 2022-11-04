# This program asks the user to enter a year and month number and then look up the
corresponding month name and number of days and display the information.
Continue accepting input until the user enters an invalid year or invalid month number.

# References: https://youtu.be/YPoxpgkftPI

def check_Leap_Year(value_Year):
    remainder = value_Year % 100
    if remainder == 0:
        remainder = value_Year % 400
        if remainder == 0:
            february = 29
        else:
            february = 28
    else:
        remainder = value_Year % 4
        if remainder == 0:
            february = 29
        else:
            february = 28    
    return february


def display_Finish():
    print("Program is stopped successfully")
    

def display_Info(value):
    print("Please enter a valid " + value + " :")
    

def display_Results(day, month, valueYear):
    print(month + " " + str(valueYear) + " has " + str(day) + " days.")
    

def get_Month_Days(value_Year, value_Month):
    days = [0] * (12)
    
    days[0] = 31
    days[1] = check_Leap_Year(value_Year)
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
    month_Days = days[value_Month - 1]
    
    return month_Days


def get_Month_Name(month_Number):
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
    month_Name = months[month_Number - 1]
    
    return monthName


def getMonths():
    displayInfo("Month")
    month = int(input())
    
    return month


def getYears():
    displayInfo("Year")
    year = int(input())
    
    return year


def main()

while True:    #This simulates a Do Loop
    valueYear = getYears()
    if valueYear >= 1:
        valueMonth = getMonths()
        if valueMonth >= 1 and valueMonth <= 12:
            day = getMonthDays(valueYear, valueMonth)
            month = getMonthName(valueMonth)
            displayResults(day, month, valueYear)
        else:
            displayFinish()
    else:
        displayFinish()
    if not(valueYear > 0 and valueMonth >= 1 and valueMonth <= 12)
    : break   
        #Exit loop
main()
