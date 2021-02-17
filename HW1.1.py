import HW1

# if you want to input your data, comment out lines 5 and 12 and comment in lines 6 and 13
def main():
    items2 = make_list2()
    # items = make_list()
    print("Here is your data:")
    print(format(" ", "^15"), end="")
    print(format("Description", "^15"), end="")
    print(format("Units", "^15"), end="")
    print(format("Price", "^15"))
    display_list(items2)
    # display_list(items)


def make_list2():
    item_list3 = []
    item1 = ["Jacket", "12", 59.95]
    item2 = ["Designer Jeans", 40, 34.95]
    item3 = ["Shirt", 20, 24.95]
    item_list2 = [item1, item2, item3]
    count2 = 0
    print("Here is data:")
    for rotation in range(1, 4):
        description = item_list2[count2][0]
        units = item_list2[count2][1]
        price = float(item_list2[count2][2])
        count2 += 1
        item_call = HW1.RetailItem(description, units, price)
        item_list3.append(item_call)
    return item_list3


def make_list():
    item_list = []
    print("Enter data for items:")
    for count in range(1, 4):
        print("Item", str(count), ":")
        description = input("Enter the description: ")
        units = input("Enter the units: ")
        price = float(input("Enter the price: $"))
        item_call = HW1.RetailItem(description, units, price)
        item_list.append(item_call)
    return item_list


"""
def display_list(item_list):
    for item in item_list:
        print(item.get_desc())
        print(item.get_units())
        print(item.get_price())
        print()
"""


def display_list(item_list):
    item_number = 1
    for item in item_list:
        print(format(("Item" + str(item_number)), "^15"), end="")
        print(format(item.get_desc(), "^15"), end="")
        print(format(item.get_units(), "^15"), end="")
        print(format(item.get_price(), "^15"))
        print()
        item_number += 1


main()
