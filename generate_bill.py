
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
"""this file just contains 1 function which take list of product as dictionary and print it in pdf file"""
def generat_bill(buy_list):
    """accept list of dictionary buy_list = [{name=,quantity=,price=,total=}}"""
    can = Canvas("bill.pdf",pagesize=A4)
    can.setFont("Times-Roman",12)
    can.drawString(9.2 *cm,28*cm,"Point Of Sale")
    can.drawString(10 *cm,27*cm,"Bill")
    can.drawString(7.6 *cm,26*cm,"List Of all Products you Bought")
    can.drawString(4*cm,24*cm,"Number")
    can.drawString(7*cm,24*cm,"Name")
    can.drawString(12*cm,24*cm,"Quantity")
    can.drawString(14*cm,24*cm,"Price")
    can.drawString(16*cm,24*cm,"Total")
    h = 23
    number = 1
    total_b = 0
    for buy in buy_list:
        nums = str(number)
        quantity = str(buy["quantity"])
        price = str(buy["price"])
        total = str(buy["total"])
        total_b += int(total)
        name = buy["name"]
        can.drawString(4*cm,h*cm,nums)
        can.drawString(7*cm,h*cm,name)
        can.drawString(12.1*cm,h*cm,quantity)
        can.drawString(14.1*cm,h*cm,price)
        can.drawString(16.2*cm,h*cm,total)
        h -=1
        number +=1
    can.drawString(4*cm,(h-3)*cm,"Total payable :"+str(total_b))     
    can.save()
