# Point of sale
- The 'Point of sale' app is a simple console app written in python programming lauguage that can be used very easily.
- The app provides mulitple actions and features for product sale management
## Features
### adding product
- first feature of this app is adding the product, the program save it in excel file and keep it permanently.
- note: if user add the same product with same price, the app track that and does not allow to be added as new product, app find the existing product and just update its quantity
### adding to existing products
- user can directly add new quantity to the existing products
### buying product
- user can see the list of products and can select anyone by product id. after selecting all the products user needed the app caculate all the price and print a pdf bill for user.
### deleting product
- app shows the list of all products and ask from user to enter id of product that he or she want ot delete.
### exiting from program
- app continue to its work until user did not terminat or close the app
## Getting started
Prerequisites:
- python interpreter must be installed in your computer
- install and import openpyxl package for adding and edit xlsx files.
- install reportlab package for pdf handling
- from reportlab.pdfgen.canvas import Canvas
- from reportlab.lib.units import cm
- from reportlab.lib.pagesizes import A4
Running App:
- open your terminal and run the following command
- Get the code:
    ```
    git clone https://github.com/AbCreativeAmid/count_and_categorize_files.git
    ```

- then enter to folder and run __init__.py file
- At first the app shows a brief description of app it shows app is insalled and working successfuly
  is installed
## How Does It Work?
- This app consist four modules product_operations.py, generat_bill.py,product.py and __init__.py
###'product_operations.py' 
- It acts somehowe like a controller between user input and product class.
- note: all these functions intract with product class for CRUD opertion
-    This file consist all the functions which do operation on products
    like:
-    -1: adding new product  :: method ==> add_product()
-    -2: getting product according to id that user enter to program :: method ==> get_product()
-    -3: add to existent products ( just update the quantities) ::: method ===> add_to 		existent_products()
    -4: buy product (do the buy process and print a pdf bill) :: method ==> buy_product()
### generat_bill.py
- """this file just contains 1 function which take list of product as dictionary and print it in pdf file"""
### product.py
- """this consist all the process of product 
-    1: product creation
-    2: product insert 
-    3: product update
-    4: product delete
-    this class directly intract with excel file for deleting, updating and inserting"""
### '__init__.py'
- """this is the main file of poject it takes show the menu to the user and handle the user request"""
## Contributing
- for any suggestion and problem in this program you can share your idea through this email hussainiabdullah786@gmail.com
### Generating Pdf bill
-in this app a modul created for generating pdf bill. by using this module generating pdf file will be so so easy.
## License
Copyright (c) AbCreativeAmid. All rights reserved.
