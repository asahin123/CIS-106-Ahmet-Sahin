def calculateCentimeters(miles):
    centimeters = miles * 160934.4
    
    return centimeters

def calculateKilometers(miles):
    kilometers = miles * 1.609344
    
    return kilometers

def calculateMeters(miles):
    meters = miles * 1609.344
    
    return meters

def displayResult(miles, kilometers, meters, centimeters):
    print(str(miles) + "Miles is " + str(kilometers) + " Kilometers " + str(meters) + " Meters " + str(centimeters) + "  Centimeters ")

def getMiles():
    print("Enter Miles")
    miles = int(input())
    
    return miles

# Main
# This program shows how to calculate the expected distance in miles to kilometers, meters, and centimeters.
miles = getMiles()
kilometers = calculateKilometers(miles)
meters = calculateMeters(miles)
centimeters = calculateCentimeters(miles)
displayResult(miles, kilometers, meters, centimeters)

# References: https://www.youtube.com/watch?v=FWaN3lTyhPU
