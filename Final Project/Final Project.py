def display_title():
    plantname = "     PLANT NAME               "  # 5-10-15
    tzones = "  ZONES      "  # 2-5-6
    tlight = "       LIGHT    "  # 7-5-4
    tprice = "    PRICE "  # 4-5-1
    line1 = "--------------------------    "  # 30
    line2 = "-----------  "  # 13
    line3 = "  --------------"  # 7-5-4
    line4 = "  --------"  # 4-5-1
    title = plantname + tzones + tlight + tprice
    lines = line1 + line2 + line3 + line4
    print(title, "\n", lines)


def display_list(name, zone, light, price):
    pnspc = "                              "
    znspc = "             "
    lgspc = "                "
    prspc = "         "
    print(name + pnspc[len(name):] + "  " + zone + znspc[len(zone):] + "  " + light + lgspc[len(light):] + price)


def display_result(item, tp):
    print_txt = "     {0} item(s)  -  ${1:.2f} Average Price"
    print(print_txt.format(item, tp/item))
    print()


def process_calculation(lpa_names, lpb_names, lp_zones, lp_light, lp_price):
    n = 0
    i = 1
    k = 1
    tp = 0
    item = 0
    lol = len(lpa_names)
    display_title()
    while k != lol:
        for j in range(i, lol):
            if lpa_names[i] == lpb_names[j]:
                k = k + 1
                item = item + 1
                tp = tp + float(lp_price[j][1:])
                display_list(lpa_names[i], lp_zones[j], lp_light[j], lp_price[j])
                # print(i, " ", j, " ", lpa_names[i], " ", lp_price[j], "B")
            else:
                display_result(item, tp)
                # print("  ==> item #: ", item, "  ", tp, "Ave :   $", tp/item, " ", "C")
                n = n + 1
                #print(n, " ", k)
                item = 0
                tp = 0
                i = j
                break
    display_result(item, tp)
    # print("  ==> item #: ", item, "  ", tp, "Ave :   $", tp / item, " ", "C")


def assign_arrays(list_plants, k):
    list_plants_items = []
    for line in list_plants:
        list_plants_items.append(line[k])
    return list_plants_items


def read_file_plant(filename):
    with open(filename, "r") as file:
        count = 0
        list_plants = []
        list_plants_title = []
        list_plants_lines = []
        for line in file:
            if count == 0:
                title = line.strip().split(",")
                list_plants_title.append(title)
                count = 1
            elif not(line.isspace()):
                lines = line.strip().split(",")
                list_plants_lines.append(lines)
        list_plants_lines.sort()
        list_plants_title.extend(list_plants_lines)
        list_plants.extend(list_plants_title)
        return list_plants


def convert_xml_to_csv():
    from xml.etree import ElementTree
    import csv

    xml = ElementTree.parse("plant_catalog.xml")  # PARSE XML

    csvfile = open("plant_catalog.csv", 'w', encoding='utf-8')  # CREATE CSV FILE
    csvfile_writer = csv.writer(csvfile)

    csvfile_writer.writerow(["Botanical", "Zone", "Light", "Price"])   # ADD THE HEADER TO CSV FILE

    for plant in xml.findall("PLANT"):  # FOR EACH PLANT
        if plant:
            # EXTRACT PLANT DETAILS
            botanical = plant.find("BOTANICAL")
            zone = plant.find("ZONE")
            light = plant.find("LIGHT")
            price = plant.find("PRICE")
            csv_line = [botanical.text, zone.text, light.text, price.text]
            csvfile_writer.writerow(csv_line)  # ADD A NEW ROW TO CSV FILE
    csvfile.close()


def main():
    convert_xml_to_csv()
    filename = "plant_catalog.csv"
    list_plants = read_file_plant(filename)
    lp_names = assign_arrays(list_plants, 0)
    lp_zones = assign_arrays(list_plants, 1)
    lp_light = assign_arrays(list_plants, 2)
    lp_price = assign_arrays(list_plants, 3)
    process_calculation(lp_names, lp_names, lp_zones, lp_light, lp_price)


main()
