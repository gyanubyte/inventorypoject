# inventory system project 

from datetime import datetime
import random
import sys

all_products = [
    [1, 'Smart Phone', 20, '20000rs'], 
    [2, 'Head Phones', 100, '300rs'], 
    [3, 'Screen Guard', 200, '50rs'], 
    [4, 'Chargers', 100, '1000rs'], 
    [5, 'Memory Cards', 120, '500rs']
]

def banner():
    print("*************")
    print("\tClix Mobiles Shop")
    print("*************")
    print("\t1.Show All Products")
    print("\t2.Buy Product")
    print("\t3.Add Products")
    print("\t4.Exit")
    print("**************")

def display_all():
    print("SNO\tProdcut\t\tIn Stock\tPrice")
    for item in all_products:
        print("{0}\t{1}\t{2}\t\t{3}".format(item[0], item[1], item[2], item[3]))

def order_summary(product, name):
    print("*****************")
    print("\t\tClix Mobiles Shop")
    print("*****************")
    print("Order Summary\tDate:{}".format(str(datetime.now())))
    print("Customer Name: {}".format(name))
    print("Product Name: {}".format(item[1]))
    print("Price: {}".format(item[-1]))
    print("*****************")
    print("\t\tTotal Bill Amount: {}".format(item[-1]))

def generate_bill(product, name):
    print("*****************")
    print("\t\tClix Mobiles Shop")
    print("*****************")
    print("Bill:{} \tDate:{}".format(int(random.random()*100000), str(datetime.now())))
    print("Customer Name: {}".format(name))
    print("Product Name: {}".format(item[1]))
    print("Price: {}".format(item[-1]))
    print("*****************")
    print("\t\tTotal Bill Amount: {}".format(item[-1]))
    


while(True):
    banner()
    choice = int(input())
    if choice == 1:
        display_all()
    elif choice == 2:
        display_all()
        prod_id = int(input("Enter the Product ID: "))
        for item in all_products:
            if item[0] == prod_id:
                name = input("Customer Name: ")
                order_summary(item, name)
                cnf = input("Confirm the Order(Y/N)")
                if cnf == 'Y':
                    item[2] -= 1
                    generate_bill(item, name)
                    print("Thanks For shopping with Us")
                    sys.exit(0)
                else:
                    print("Continue Exploring the shop")
    elif choice == 3:
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":
            prod = []
            prod.append(len(all_products)+1)
            prod.append(input("Enter the Product Name: "))
            prod.append(int(input("Available: ")))
            prod.append(int(input("Price: ")))
            all_products.append(prod)
        else:
            print("Incorrect username and password")
    else:
        print("GoodBye!!")
        break