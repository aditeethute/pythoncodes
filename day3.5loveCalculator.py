#day3.5 LOVE CALCULATOR 
#take both people name check the no. of times the letters in word 'TRUE' and word 'LOVE' occurs then conbine these numbers to make 2 digit number
n1=input("enter your name: ").lower()
n2=input("enter thier name: ").lower()
c=n1+n2#couple name 
t=c.count("t")
r=c.count("r")
u=c.count("u")
e=c.count("e")
p1= int(t)+int(r)+int(u)+int(e)
l=c.count("l")
o=c.count("o")
v=c.count("v")
e=c.count("e")
p2=int(l)+int(o)+int(v)+int(e)
per=str(p1)+str(p2)
p=int(per)
if p<10 or p>90:
    print(f"your score is {per}%, you go together like coke and mentos;).")
elif p>=40 and p<=50:
    print(f"your score is {per}%, you are right together:).") 
else :
    print(f"your score is {per}%")  
 
