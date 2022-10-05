# Create a program that asks the user for a distance in miles, and then ask the user if they want the distance in US measurements (yards, feet, and inches) or in metric measurements (kilometers, meters, and centimeters). Use if/else conditional statements to determine their selection and then calculate and display the results.

# References: https://www.youtube.com/watch?v=VcZG_PxP7wQ&t=34s

def displayResult(miles, kmeterORyard, scaleKmORyard, meterORfeet, scaleMeterORfeet,
                  cmORinches, scaleCmORinches):
    print(str(miles) + " mile(s) is equivalent to " + str(kmeterORyard) 
          + scaleKmORyard + str(meterORfeet) + scaleMeterORfeet + str(cmORinches) + scaleCmORinches)

def getChoiceChar():
    print("Enter U to convert to US distance or M to convert to Metric distance.")
    choice = input()
    
    return choice
  
def getInputMiles():
    print("Enter the expecting miles")
    miles = input()
    
    return miles
  
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

def processMetricDistance(miles):
    kilometers = calculateKilometers(miles)
    meters = calculateMeters(miles)
    centimeters = calculateCentimeters(miles)
    displayResult(miles, kilometers, " km, ", meters, " m, ", centimeters, " cm.")

def processUsDistance(miles):
    yards = calculateYards(miles)
    feet = calculateFeet(miles)
    inches = calculateInches(miles)
    displayResult(miles, yards, " yards, ", feet, " ft, ", inches, " inches.")

# Main
miles = getInputMiles()
choice = getChoiceChar()
if choice == "U" or choice == "u":
    processUsDistance(miles)
else:
    if choice == "M" or choice == "m":
        processMetricDistance(miles)
    else:
        print("You must enter U to convert distance into US distance or M to convert into Metric distance!")


