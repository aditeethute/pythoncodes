#day3 of 100days of code
#conditional statement, Logical opretor, Code blocks and Scope
#if/else statement
#who can ride rolercoster base on their height
print("wellcome to the rolercoster ride")
h=input("please enter your height in cm: ")
if int(h)>=120:
    print("please go ahead, you can ride ")
else:
    print("We are sry! but, you cann't ride ") 
#day3.1 Odd or Even
#check if the number enter is odd or even
n=int(input("enter the integer number: "))
r=int(n%2)
print(r)
if r==0:
    print(f"entered number {n} is an even number.")
else:
    print(f"entered number {n} is an odd number.")  
#nested if/else statement
#on rolercoster ride after checking height check for the money the user have to pay according to their age (above 18 12/-, between 18-12=10/-, below 12 5/-)
print("wellcome to the rolercoster ride")
height=input("please enter your height in cm: ")
age=int(input("please enter your age"))
if int(height)>=120:
    if age>=18:
       print("please go ahead, you can ride. pls pay 12/- ")
    else:
        if age>+12:
          print("please go ahead, you can ride. pls pay 10/-")   
        else:
          print("please go ahead, you can ride. pls pay 5/-")
else:
    print("We are sry! but, you cann't ride ")
#multiple if condition
#in same rolercoster exercise add if the the person want to have a photo
ht=input("please enter your height in cm: ")
a=int(input("please enter your age"))
if int(ht)>=120:
    print("you can go for the ride, but before that let us know if u like to have a picture of yours on the ride.")
    pic=int(input("enter 1 for YES and 2 for NO"))
    if pic==2:
      if a>=18:
       print("please go ahead, you can ride. pls pay 12/- ")
      else:
        if a>+12:
          print("please go ahead, you can ride. pls pay 10/-")   
        else:
          print("please go ahead, you can ride. pls pay 5/-")
    elif pic==1:
        if a>=18:
          print("please go ahead, you can ride. pls pay in total 12+3=15/- ")
        else:
          if a>+12:
           print("please go ahead, you can ride. pls pay in total 10+3=13/-")   
          else:
           print("please go ahead, you can ride. pls pay in total 5+3=8/-")
else:
    print("We are sry! but, you cann't ride ")
#or
print("wellcome to the rolercoster ride")
height=input("please enter your height in cm: ")
age=int(input("please enter your age"))
if int(height)>=120:
    print("let us know if you want a picture.")
    pic=input("enter y if you want or enter n fi you don't: ")
    if age>=18:
       bill=12
       print("please go ahead, you can ride. pls pay 12/- ")
    else:
        if age>+12:
          bill=10
          print("please go ahead, you can ride. pls pay 10/-")   
        else:
          bill=5
          print("please go ahead, you can ride. pls pay 5/-")
    if pic=="y":
       bill+=3
       print(f"due to picture your new in total bill is: {bill}")  

else:
    print("We are sry! but, you cann't ride ")

#logical oprator
#for the same above rolercoster ticketing, add new condition that the person with midlife crisis(45-55 age) tickets are free
print("wellcome to the rolercoster ride")
height=input("please enter your height in cm: ")
age=int(input("please enter your age"))
if int(height)>=120:
    print("let us know if you want a picture.")
    pic=input("enter y if you want or enter n fi you don't: ")
    if age>=18:
       bill=12
       print("please go ahead, you can ride. pls pay 12/- ")
    else:
        if age>+12:
          bill=10
          print("please go ahead, you can ride. pls pay 10/-")   
        else:
          bill=5
          print("please go ahead, you can ride. pls pay 5/-")
    if pic=="y":
       bill+=3
    if age<=55 and age>=45:
      bill=0
      print("your bill is of 0/- as you are in midlife crisis.")   
    print(f"due to picture your new in total bill is: {bill}")  
else:
  print("We are sry! but, you cann't ride ")
 
    



