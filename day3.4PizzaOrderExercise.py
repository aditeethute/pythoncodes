#DAY3.4
#pythonpizza, to build the automatic pizza order.
#the experiment will ask the customer the size of pizza,ask for pepperoni and for the extra cheese, and a/c to the order, work out their final bill.
print("wellcome to the Python Pizza Order Taker and Deliveries!")
size=input ("Please enter the size of the pizza.\n(small-s,medium-m,large-l): ")
p=input("let us know if you like us to want pepperoni\n(yes-y,no-n): ")
c=input("do you want to add some extra cheese?\n(yes-y/no-n): ")
bill=0
if size=="s":
    bill+=15
elif size=="m":
    bill+=20
else :
    bill+=25        
if p=="y":
    if size=="s":
        bill+=2
    elif size=="m": 
        bill+=3
    else :
        bill+=3
if c=="y":
    bill+=1
else:
    bill+=0
print(f"the bill for your order is: {bill}") 
  


