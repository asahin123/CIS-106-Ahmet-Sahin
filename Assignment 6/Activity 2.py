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

def displayResult(age, months, days, hours, seconds):
    print(str(age) + "Age is " + str(months) + "Months " + str(days) + "Days " + str(hours) + "Hours " + str(seconds) + "Seconds ")

def getAge():
    print("Enter Age")
    age = int(input())
    
    return age

# Main
# This program shows an expected age in months, days, hours, and seconds.
age = getAge()
months = calculateMonths(age)
days = calculateDays(age)
hours = calculateHours(age)
seconds = calculateSeconds(age)
displayResult(age, months, days, hours, seconds)

# References: https://www.youtube.com/watch?v=FWaN3lTyhPU
