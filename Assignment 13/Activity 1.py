# This program asks the user for a single line of text containing a first name 
# and last name and print out the name in the form last name,
# first initial, such as Lastname, F.

# References: https://www.w3schools.com/python/python_strings.asp

def get_full_name():
    fullname = input(" Firstname Lastname : ")
    return fullname


def process_full_name(fullname):
    name_list = fullname.split()
    name = name_list[-1].title() + ", " + name_list[0][0:1].title() + "."
    return name


def display_full_name(processed_name):
    print(processed_name)
    return


def main():
    fullname = get_full_name()
    processed_name = process_full_name(fullname)
    display_full_name(processed_name)
    

main()
