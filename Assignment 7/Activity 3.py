# This program asks the user to select US or Metric conversion and input a given distance. Then the program converts the given distance to miles and displays the result.

# References: https://www.youtube.com/watch?v=VcZG_PxP7wQ&t=34s

def calculateCentimeters(miles):
    centimeters = miles * 160934.4
    
    return centimeters

def calculateFeet(miles):
    feet = miles * 5280
    
    return feet

def calculateInches(miles):
    inches = miles * 63360
    
    return inches

def calculateKilometers(miles):
    kilometers = miles * 1.609344
    
    return kilometers

def calculateMeters(miles):
    meters = miles * 1609.344
    
    return meters

def calculateYards(miles):
    yards = miles * 1760
    
    return yards

def displayResult(miles, kMyD, strKm, mTfT, strM, cMiN, strCm):
    print(str(miles) + " mile(s) is equivalent to " + str(kMyD) + strKm + str(mTfT) + strM + str(cMiN) + strCm)

def getChoiceChar():
    print("Enter US to convert to US distance or Metric to convert to Metric distance.")
    choice = input()
    
    return choice

def getInputMiles():
    print("Enter distance in terms of miles")
    miles = input()
    
    return miles

def processMetricDistance(miles):
    kilometers = calculateKilometers(miles)
    meters = calculateMeters(miles)
    centimeters = calculateCentimeters(miles)
    displayResult(miles, kilometers, " kilometers, ", meters, " meters, ", centimeters, " centimeters.")

def processUsDistance(miles):
    yards = calculateYards(miles)
    feet = calculateFeet(miles)
    inches = calculateInches(miles)
    displayResult(miles, yards, " yards, ", feet, " ft, ", inches, " inches.")

# Main

choice = getChoiceChar()
miles = getInputMiles()
if choice == "US" or choice == "us":
    processUsDistance(miles)
else:
    if choice == "Metric" or choice == "metric":
        processMetricDistance(miles)
    else:
        print("You must enter US to convert distance into US distance or Metric to convert into Metric distance!")


