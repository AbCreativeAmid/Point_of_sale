from product_operations import *
"""this is the main file of poject it takes show the menu to the user and handle the user request"""

def request_for_input():
    """show menu to the user and ask user for input and validate the input"""
    #select menu option:// this function returns the option user select
    print("\n")
    print("1:Add Product"+" "*7+"2:Add to existent products"+" "*2+"3:Bye Product"+" "*7+"4:Delete Product"+" "*4+"5:Exit Product"+" "*6)
    print("\n")
    operation = input("Select one of above!_  ")
    try:
        operation = eval(operation)
        return operation
    except:
        print("Enter a number!_ ")
        return 0

input("Hello welcome to Point of Sale Programm!_  (press Enter!)  ")
input("You can Add, Buy or delete the products through this program! please press Enter for Menu Display!_  ")
input("Select from the following menue what want to do!_  (press Enter!)  ")
#it iterate the process until the user does not end the program
while True:
    op = request_for_input()
    if op ==1:
        add_product()
    if op ==2:
        add_to_existent_products()
    elif op ==3:
        buy_product()
    elif op ==4:
        delete_product()
    elif op == 5:
        break
print("thanks for using! bye have a good time!  ")
