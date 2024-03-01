#day15 coffee machine poject## there r 3 type of coffee here::EPRESSO-50ml h2o,18g coffee ::LATTE-200ml h20, 24g coffee, 150ml milk::CAPPUCCINO- 250ml water, 24g coffee, 100ml milk 
##features of coffee machine #coffee machine already have some resources they are- 300ml of h20, 200ml of mikl, 100g of coffee# COIN OPERATED - here we are going to use 4 types of coin PENNY-1CENT($0.01),NICKEL-5CENTS,DIME-10CENTS,QUARTER-25CENTS.

logo="""                      //  ) ) //  ) )                                                                                      (         
    ___      ___   __//__  __//__  ___      ___          _   __      ___      ___     / __     ( )   __      ___         __)__ 
  //   ) ) //   ) ) //      //   //___) ) //___) )     // ) )  ) ) //   ) ) //   ) ) //   ) ) / / //   ) ) //___) )   C\|     \ 
 //       //   / / //      //   //       //           // / /  / / //   / / //       //   / / / / //   / / //            \     /
((____   ((___/ / //      //   ((____   ((____       // / /  / / ((___( ( ((____   //   / / / / //   / / ((____          \___/ """
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
print("Wellcome to the Coffee Machine:) we are happy to have you here!")

again=True
while again==True:
    a=int(0)
    print(f"{logo}")
    def money():
        p=n=d=q=int(0)
        p=int(input("number of penny you enter: "))#penny
        n=int(input("number of nikel you enter: "))#nickel
        d=int(input("number of dime you enter: "))#dime
        q=int(input("number of quarter you enter: "))#quarter
        m=(p*1)+(n*5)+(d*10)+(q*25)
        return m
    choice=input("what would you like to have?(Espresso/Latte/Cappuccino)?: ").lower()
    if choice=="espresso":
        if resources["coffee"]>MENU["espresso"]["ingredients"]["coffee"]and  resources["water"]>MENU["espresso"]["ingredients"]["water"] :
            resources["water"]-=50
            resources["coffee"]-=18
            print(f"you need to pay-1.5 cents")
            a=int(money())
            if MENU["espresso"]["cost"]<=float(a):
                rm=float(a)-MENU["espresso"]["cost"]
                print(f"your change={rm}")
            else:
                print("sry but you didim't pay the enough money")
            
        else:
            print("we are so sry!! but it look like we don't have enough resources...:|")

    elif choice=="latte":
        if resources["coffee"]>MENU["latte"]["ingredients"]["coffee"] and  resources["milk"]>MENU["latte"]["ingredients"]["milk"] and  resources["water"]>MENU["latte"]["ingredients"]["water"] :
            resources["water"]-=200
            resources["coffee"]-=24
            resources["milk"]-=150
            print(f"you need to pay-2.5 cents")
            a=int(money())
            if MENU["latte"]["cost"]<=float(a):
                rm=float(a)-MENU["latte"]["cost"]
                print(f"your change={rm}")
            else:
                print("sry but you didim't pay the enough money")
        else:
            print("we are so sry!! but it look like we don't have enough resources...:|")

    elif choice=="cappuccino":
        if resources["coffee"]>MENU["cappuccino"]["ingredients"]["coffee"]and  resources["milk"]>MENU["cappuccino"]["ingredients"]["milk"]and  resources["water"]>MENU["cappuccino"]["ingredients"]["water"]  :
            resources["water"]-=250
            resources["coffee"]-=24
            resources["milk"]-=100
            print(f"you need to pay-3.0 cents")
            a=int(money())
            if MENU["cappuccino"]["cost"]<=float(a):
                rm=float(a)-MENU["cappuccino"]["cost"]
                print(f"your change={rm}")
            else:
                print("sry but you didim't pay the enough money")
        else:
            print("we are so sry!! but it look like we don't have enough resources...:|")

    elif choice=="report":
        print(resources)
    else:
        print("you enter something invaild:|")

    coun=input("do you need something else?(yes/no):")
    if coun=="no":
        again=False
        print("thank you for visiting we are looking forward to serve you again:)")
    elif coun=="yes":
        import os
        os.system('cls')


