from insert import *
from update import *
from delete import *
from select import *

def print_menu():
    print ('1. show customers ')
    print ('2. add customers ')
    print ('3. remove a customers')
    print ('4. update a customers')
    print ('5. quit')
    print ('press any key to show menu')
    print ()

def insertcustomer ():
    print ("add customer : ")
    customername = input("firstName :")
    customerfamily = input("lastName :")
    nationalcode = input("nationalCode :")
    insert(customername,customerfamily,nationalcode)

def selectcustomer():
    print ("customers are :")
    select()

def updatecustomer():
    print ("update customer :")
    nationalcode = input("enter customer national code :")
    customername = input("enter new name : ")
    update(nationalcode,customername)

def deletecustomer():
    print("delete customer :")
    nationalcode = input("enter customer nationalcode :")
    delete(nationalcode)

menu_choice = 0
print_menu()
while menu_choice !=5:
    menu_choice = input("type number 1-5 :")

    if menu_choice == "1":
        selectcustomer()
    elif menu_choice == "2":
        insertcustomer()
    elif menu_choice == "3":
        deletecustomer()
    elif menu_choice == "4":
        updatecustomer()
    elif menu_choice == "5":
        break






