# This program shows how to calculate the expected distance in miles
# into kilometers, meters, and centimeters.

# References: 
#   For this session, I took help from my friend who also does coding.

print("Enter miles:")
miles = int(input())

kilometers = miles * 1.609344
meters = miles * 1609.344
centimeters = miles * 160934.4

print("kilometers=" + str(kilometers))
print("meters=" + str(meters))
print("centimeters=" + str(centimeters))
