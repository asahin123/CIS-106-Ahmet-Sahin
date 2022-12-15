# This program shows the lists of the plants for their
# common name, botanical name, zone,
# light, and prices and taken the average price for every item.

# References: https://youtu.be/pTB0EiLXUC8


def display_result(number_of_items, total_price):
    try:
        print()
        text = "     {0} item(s)  -  ${1:.2f} Average Price"
        print(text.format(number_of_items, total_price / number_of_items))
    except ZeroDivisionError:
        print("Missing or bad data")
        raise SystemExit


def display_plant_list(common_name, botanical_name,
                       zone_name, light_name, price_name):
    title_part_1 = common_name + " (" + botanical_name + ")" + " - "
    title_part_2 = zone_name + " - " + light_name + " - " + price_name
    print(title_part_1 + title_part_2)


def process_calculation(common, botanical, zone, light, price):
    total_price = 0
    number_of_items = 0
    for x in range(1, len(common) - 1):
        display_plant_list(common[x], botanical[x],
                           zone[x], light[x], price[x])
        total_price = total_price + float(price[x].lstrip("$"))
        number_of_items = number_of_items + 1
    display_result(number_of_items, total_price)


def list_plants(filename):
    import re
    common = []
    botanical = []
    zone = []
    light = []
    price = []
    common.append("Common Name")
    botanical.append("Botanical Name")
    zone.append("Zone")
    light.append("Light")
    price.append("Price")
    try:
        with open(filename, "r") as file:
            for line in file:
                if re.search("COMMON", line):
                    common.append(line[line.find(">") + 1:line.find("/") - 1])
                if re.search("BOTANICAL", line):
                    botanical.append(line[line.find(">")
                                          + 1:line.find("/") - 1])
                if re.search("ZONE", line):
                    zone.append(line[line.find(">") + 1:line.find("/") - 1])
                if re.search("LIGHT", line):
                    light.append(line[line.find(">") + 1:line.find("/") - 1])
                if re.search("PRICE", line):
                    price.append(line[line.find(">") + 1:line.find("/") - 1])
    except Exception as messages:
        print("missing or bad data")
    process_calculation(common, botanical, zone, light, price)


def load_xml(filename):
    import urllib.request
    url = 'https://www.w3schools.com/xml/plant_catalog.xml'
    try:
        page = urllib.request.urlopen(url).read().decode()
    except Exception as exception:
        print(str(exception) + " reading " + url)
        raise SystemExit


def main():
    filename = 'plant_name_list.xml'
    load_xml(filename)
    list_plants(filename)


main()
