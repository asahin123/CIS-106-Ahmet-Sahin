# This program asks the user to enter a year and month number and then look up the corresponding\
month name and number of days and display the information.\
Continue accepting input until the user enters an invalid year or invalid month number.

# References: https://youtu.be/YPoxpgkftPI

def checkLeapYear(valueYear):
    remainder = valueYear - int(float(valueYear) / 100) * 100
    if remainder == 0:
        remainder = valueYear - int(float(valueYear) / 400) * 400
        if remainder == 0:
            february = 29
        else:
            february = 28
    else:
        remainder = valueYear - int(float(valueYear) / 4) * 4
        if remainder == 0:
            february = 29
        else:
            february = 28
    
    return february


def displayFinish():
    print("Program is stopped successfully")

    
def displayInfo(value):
    print("Please enter a valid " + value + " :")

    
def displayResults(day, month):
    print(month + " " + str(valueYear) + " has " + str(day) + " days.")

    
def getMonthDays(valueYear, valueMonth):
    days = [0] * (12)
    
    days[0] = 31
    days[1] = checkLeapYear(valueYear)
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
    monthDays = days[valueMonth - 1]
    
    return monthDays


def getMonthName(monthNumber):
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
    monthName = months[monthNumber - 1]
    
    return monthName


def getMonths():
    displayInfo("Month")
    month = int(input())
    
    return month


def getYears():
    displayInfo("Year")
    year = int(input())
    
    return year


# Main
while True:    #This simulates a Do Loop
    valueYear = getYears()
    if valueYear >= 1:
        valueMonth = getMonths()
        if valueMonth >= 1 and valueMonth <= 12:
            day = getMonthDays(valueYear, valueMonth)
            month = getMonthName(valueMonth)
            displayResults(day, month)
        else:
            displayFinish()
    else:
        displayFinish()
    if not(valueYear > 0 and valueMonth >= 1 and valueMonth <= 12):
        break   #Exit loop
