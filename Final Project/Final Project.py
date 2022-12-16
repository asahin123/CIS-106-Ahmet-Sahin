# This program shows the lists of the plants for their
# common name, botanical name, zone,
# light, and prices and taken the average price for every item.

# References: https://youtu.be/pTB0EiLXUC8


def display_result(number_of_items, total_price):
    try:
        print()
        text = "{0} items - ${1:.2f} average price"
        print(text.format(number_of_items, total_price / number_of_items))
    except ZeroDivisionError:
        print("Division by Zero because of the variable is zero")
        raise SystemExit


def display_plant(common, botanical, zone, light, price):
    text = "{0} ({1}) - {2} - {3} - {4}"
    print(text.format(common, botanical, zone, light, price))


def process_calculation(common, botanical, zone, light, price):
    total_price = 0
    number_of_items = 0
    try:
        for x in range(len(common)):
            display_plant(common[x], botanical[x], zone[x], light[x], price[x])
            total_price = total_price + float(price[x].lstrip("$"))
            number_of_items = number_of_items + 1
        display_result(number_of_items, total_price)
    except IndexError:
        print()
        print("Error: Missing or bad data.")
        raise SystemExit
    except AssertionError:
        print("Error: Missing or bad data.")
        raise SystemExit
    except TypeError as e:
        print(e)


def list_plants(filename):
    import re

    common = []
    botan = []
    zone = []
    light = []
    price = []
    try:
        with open(filename, "r") as file:
            for line in file:
                if re.search("COMMON", line):
                    common.append(line[line.find(">") + 1:line.find("/") - 1])
                if re.search("BOTANICAL", line):
                    botan.append(line[line.find(">") + 1:line.find("/") - 1])
                if re.search("ZONE", line):
                    zone.append(line[line.find(">") + 1:line.find("/") - 1])
                if re.search("LIGHT", line):
                    light.append(line[line.find(">") + 1:line.find("/") - 1])
                if re.search("PRICE", line):
                    price.append(line[line.find(">") + 1:line.find("/") - 1])
    except FileNotFoundError:
        msg = "the file " + filename + " is not found"
        print(msg)
    else:
        process_calculation(common, botan, zone, light, price)


def load_xml(filename):
    import urllib.request

    url = "https://www.w3schools.com/xml/plant_catalog.xml"
    try:
        page = urllib.request.urlopen(url).read().decode()
        with open(filename, 'w') as file_name:
            file_name.write(str(page))
    except Exception as exception:
        print(str(exception) + " reading " + url)
        raise SystemExit


def main():
    filename = 'plant_catalog.xml'
    load_xml(filename)
    list_plants(filename)


main()
