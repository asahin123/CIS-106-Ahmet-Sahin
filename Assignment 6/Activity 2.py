def calculateDays(age):
    days = age * 365
    
    return days

def calculateHours(age):
    hours = age * 8760
    
    return hours

def calculateMonths(age):
    months = age * 12
    
    return months

def calculateSeconds(age):
    seconds = age * 31536000
    
    return seconds

def calculateYears(age):
    years = age
    
    return years

def displayResult(months, days, hours, seconds):
    print(str(months) + " Months " + str(days) + " Days " + str(hours) + " Hours " + str(seconds) + " Seconds ")

def getAge():
    print("Enter Age")
    age = int(input())
    
    return age

# Main
# This program shows an expected age in months, days, hours, and seconds.
age = getAge()
years = calculateYears(age)
months = calculateMonths(age)
days = calculateDays(age)
hours = calculateHours(age)
seconds = calculateSeconds(age)
displayResult(months, days, hours, seconds)

# References: https://www.youtube.com/watch?v=FWaN3lTyhPU
