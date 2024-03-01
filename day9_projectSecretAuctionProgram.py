#day9 project 
#SECRET AUCTION PROGRAM
print("                         ___________")
print("                         \         /")
print("                          )_______(")
print("                          |+++++++|_,-,_,----------,._,-,.    ")
print("                          |       | | |               | | ''-. ")
print("                          |       |_| |_             _| |_..-' ")
print("                          |_______| '-' `'---------'` '-'")
print("                          )++++++++ ")
print("                         /_________\ ")
print("                         `'-------'` ")
print("                       .-------------.")
print("                      /_______________\ ")
print("    WELLCOME TO THE SECRECT AUCTIONS!! we are glad to have you today!")
bid_record=[]
import os
g=True
while g==True:
    def add():
        name=input("sir/ma'am please enter your name here: ")
        bid=input("how much would you like to bid: ")
        record={}
        record["name"]=name
        record["bid"]=bid
        bid_record.append(record)
    add()
    yn=input("do anyone else want to bid?*yes OR no*: ")
    if yn=="no":
        g=False
        os.system('cls')
    elif yn=="yes":
        os.system('cls')
    else:
        os.system('cls')
        print("Oops!! you enter something worng, plz try it again.")

print(bid_record)
#checking the highest bid
value=int(0)
for n in range(len(bid_record)):
    c=bid_record[n]
    if int(value)<int(c["bid"]):
        value=c["bid"]
winner=""
for n in range(len(bid_record)):
    c=bid_record[n] 
    if int(value)==int(c["bid"]):
        winner=str(c["name"])
         
print(f"The highest bid was of {value}\- ,CONGRATULATIONS!!! to the winner {winner} for winning the auction. ")
print("                                                                       88")    
print("                                                                       88 ")    
print(" ,adPPYba,  ,adPPYba,  8b,dPPYba,   ,adPPYb,d8 8b,dPPYba, ,adPPYYba, MM88MMM  ,adPPYba, ")   
print("a8*      ` a8"     "8a 88P'   ``8a a8`    `Y88 88P'   `Y8 ""     `Y8   88     I8[    ""  ")    
print("8b         8b       d8 88       88 8b       88 88         ,adPPPPP88   88      `*Y8ba,   ")   
print("`8a,   ,aa `8a,   ,a8` 88       88 `8a,   ,d88 88         88,    ,88   88,    aa    ]8I   ")   
print(" ``Ybbd8`'  ``YbbdP``  88       88  ``YbbdP`Y8 88         `88bbddp``   `*888  `*YbbdP`` ")  
print("                                    aa,    ,88  ")                               
print("                                     `Y8bbdP`  ")                              
           
           
           
           
