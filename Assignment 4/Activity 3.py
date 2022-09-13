# This program shows how to calculate the expected distance in kilometers, meters, and centimeters.

miles = int(input())

distance = miles
kilometers = miles * 1.609344
meters = miles * 1609.344
centimeters = miles * 160934.4

print(" kilometers=" + str(kilometers)),
print(" meters=" + str(meters)),
print(" centimeters=" + str(centimeters)),
