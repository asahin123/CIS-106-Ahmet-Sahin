# This program shows the lists of the plants for their
# common name, botanical name, zone,
# light, and prices and taken the average price for every item.

# References: https://youtu.be/pTB0EiLXUC8


def list_plants(filename, tag):
    import re

    array = []
    try:
        with open(filename, "r") as file:
            for line in file:
                if re.search(tag, line):
                    array.append(line[line.find(">") + 1:line.find("/") - 1])
        return array
    except FileNotFoundError:
        print("File is missing")
        exit()


def process_calculation(price):
    total_price = 0
    try:
        for x in range(len(price)):
            total_price = total_price + float(price[x].lstrip("$"))

        average_price = total_price / len(price)

        return average_price
    except IndexError:
        print()
        print("Error: Missing or bad data.")
        raise SystemExit
    except ZeroDivisionError:
        print("Error: Missing or bad data.")
        raise SystemExit
    except ValueError:
        print("Error: Missing or bad data.")
        raise SystemExit
    except TypeError as e:
        print(e)
    except FileNotFoundError:
        print("File is missing")


def display_plant(common, botanical, zone, light, price):
    try:
        for index in range(len(common)):
            text = "{0} ({1}) - {2} - {3} - {4}"
            print(text.format(
                common[index], 
                botanical[index], 
                zone[index], 
                light[index], 
                price[index]))
    except IndexError:
        print()
        print("Error: Missing or bad data.")
        raise SystemExit
    except AssertionError:
        print("Error: Missing or bad data.")
        raise SystemExit
    except TypeError as e:
        print(e)
    except FileNotFoundError:
        print("File is missing")


def display_result(number_of_items, average_price):
    if number_of_items == 0:
        print("File is empty, missing, or has bad data")

    try:
        print()
        text = "{0} items - ${1:.2f} average price"
        print(text.format(number_of_items, average_price))
    except ZeroDivisionError:
        print("Division by Zero because of the variable is zero")
        raise SystemExit


def main():
    filename = 'plant_catalog.xml'
    common = list_plants(filename, "COMMON")
    botanical = list_plants(filename, "BOTANICAL")
    zone = list_plants(filename, "ZONE")
    light = list_plants(filename, "LIGHT")
    price = list_plants(filename, "PRICE")

    number_of_items = len(price)
    average_price = process_calculation(price)

    display_plant(common, botanical, zone, light, price)
    display_result(number_of_items, average_price)


main()
