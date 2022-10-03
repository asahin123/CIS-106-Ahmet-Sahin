def getChoiceChar():
    print("Enter U to convert to US distance or M to convert to Metric distance.")
    choice = input()
    
    return choice

def getInputMiles():
    print("Enter distance in terms of miles")
    miles = float(input())
    
    return miles

def processMetricDistance(miles):
    kilometers = miles * 1.609344
    meters = miles * 1609.344
    centimeters = miles * 160934.4
    print(str(miles) + " mile(s) is equivalent to " + str(kilometers) + " km, " + str(meters) + " m, " + str(centimeters) + " cm")

def processUsDistance(miles):
    yards = miles * 1760
    feet = miles * 5280
    inches = miles * 63360
    print(str(miles) + " mile(s) is equivalent to " + str(yards) + " yards, " + str(feet) + " ft, " + str(inches) + " inches")

def main():
miles = getInputMiles()
choice = getChoiceChar()
if choice == "U" or choice == "u":
    processUsDistance(miles)
else:
    if choice == "M" or choice == "m":
        processMetricDistance(miles)
    else:
        print("You must enter U to convert distance into US distance or M to convert into Metric distance!")
        
main()
