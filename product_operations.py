from openpyxl import load_workbook,worksheet
from product import *
from generate_bill import *
""" It acts somehowe like a controller between user input and product class.
    note: all these functions intract with product class for CRUD opertion
    This file consist all the functions which do operation on products
    like:
    1: adding new product  :: method ==> add_product()
    2: getting product according to id that user enter to program :: method ==> get_product()
    3: add to existent products ( just update the quantities) ::: method ===> add_to existent_products()
    4: buy product (do the buy process and print a pdf bill) :: method ==> buy_product()
    """
def add_product():
    """add new product to excel file"""
    print("====================================  1: Add Product ===================================")
    Product.display_products()
    input("For new product please add the following details!  (press Enter!)  ")
    #loop for adding more and more products until user does not terminat adding process
    while True:
        #getting detials of product as input
        name = input("Enter the name of product!_    ")
        quantity = input("Enter amount of product!_  ")
        price = input("Enter prict of product!_      ")

        #creating product object
        product = Product(name,quantity,price)
        product.insert_product()
        Product.display_products()
        #asking for add another product
        response = input("Want to add more (Y/N)")
        #if Y or y loop while begins from begining
        if response in ["y","Y"]:
            continue
        #any other input will terminat the process of adding and go to main menu
        else:
            break

def get_product():
    
    """fetching the product according to id that user entered and returns the product and quantity user entered as tuple (product,quantity)"""
    print("Check the bellow list of product")
    #reading producst from file and listing them
    Product.display_products()
    #getting id of product from user
    id = input("Enter the id of product!_  or press N for cancel! ")
    #validating id must be integer
    try:
        id = eval(id)
    except:
        if id in ["N","n"]:
            return "terminate"
        id =print("Enter valid id!_   ")
        return "skip"
    
    #creating null product Object
    product = Product()
    #initialling product by using product id
    product.get_details(id)
    invalidInput = False
    #getting and validating quantity
    try:
        quantity = eval(input("Enter the quantity you want!_   "))
    except:
        print("invalid Input( more than existent quantity or is string! -----")
        invalidInput = True
    #quatity must be less than existing quatity
    while int(product.quantity)<quantity or invalidInput:
        quantity = input("Enter the valid quantity( more than existent quantity)!_ or N for Skipping ")
        try:
            quantity = eval(quantity)
            invalidInput = False
        except:
            if quantity in["N","n"]:
                quantity = 0
                invalidInput = True
            break
    return (product,quantity)

def add_to_existent_products():
    print("====================================  2: Add To Existent Products ===================================")
    """Just update the quantity of exsitent products """
    while True:
        #get product return skip or terminate or a tuple(product,quantity)
        response = get_product()
        if response =="skip":
            continue
        elif response == "terminate":
            break
        else:
            #update the quantity and adding new quantity on existent quantity
            product,quantity = response[0],response[1]
            if int(product.id) != 0:
                product.update_product(-quantity)
                Product.display_products()
        #asking for to add another product
        response = input("Want to add more (Y/N)")
        if response in ["y","Y"]:
            continue
        else:
            break

def buy_product():
    """get product and quantity from get_product function and create a list of buy products
        then print the list in pdf file with total amount and bought list """
    print("====================================  3: Buy ===================================")
    buy_list = []
    while True:
        response = get_product()
        if response =="skip":
            continue
        elif response == "terminate":
            break
        else:
            product,quantity = response[0],response[1]
            #if quantity be more than 0 it will be added to buy list as a dictionary 
            #and quantity of product will be updated and deducted
            if quantity > 0 and int(product.id)!=0:
                buy_list.append({"id":id,"name":product.name,"quantity":quantity,"price":product.price,"total":int(quantity)*int(product.price)})
                product.update_product(quantity)
            #want more product or no
            response = input("Want more? (Y/N)")
            if response in ["y","Y"]:
               continue
            else:
                if len(buy_list)>0:
                    print("\n Your bill printed in pdf format! \n ")
                break
    #generating bill
    generat_bill(buy_list)

def delete_product():
    print("====================================  4: Delete Product ===================================")
    """ask for product id and then remove it the whole row in excel file"""
    while True:
        #reading producst from file and listing them
        Product.display_products()

        id = input("Enter the id of product you want to delete!_  or press N for cancel!  ")
        #validating id must be integer
        try:
            id = eval(id)
        except:
            if id in ["N","n"]:
                break
            print("Enter valid id!_   ")
            continue
        product = Product()
        #loading excel file for deleting product
        products_file = load_workbook("products.xlsx")
        products = products_file.active
        #product details fetched by id 
        product.get_details(id)
        if int(product.id) != 0:
            #selected product deleted
            products.delete_rows(product.row)
            #then save the file
            products_file.save("products.xlsx")
            print("Successfully Deleted!_  ")

            Product.display_products()
            #want more product or no
            response = input("Want to delete more? (Y/N)   ")
            if response in ["y","Y"]:
                continue
            else:
                break