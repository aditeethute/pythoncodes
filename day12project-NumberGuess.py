from typing import Container


logo=""".__   __.  __    __  .___  ___. .______    _______ .______           _______  __    __   _______     _______.     _______.
|  \ |  | |  |  |  | |   \/   | |   _  \  |   ____||   _  \         /  _____||  |  |  | |   ____|   /       |    /       |
|   \|  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |       |  |  __  |  |  |  | |  |__     |   (----`   |   (----`
|  . `  | |  |  |  | |  |\/|  | |   _  <  |   __|  |      /        |  | |_ | |  |  |  | |   __|     \   \        \   \    
|  |\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \----.   |  |__| | |  `--'  | |  |____.----)   |   .----)   |   
|__| \__|  \______/  |__|  |__| |______/  |_______|| _| `._____|    \______|  \______/  |_______|_______/    |_______/    
                                                                                                                          """
print(f"{logo}\n Wellcome to game of NUMBER GUESS!!!\n here you have to guess the number between 1 to 100")
cont=True
while cont==True:
    import random
    a=random.randint(1,100)
    print(a)
    def guess():
        g=int(input("enter your guess: "))
        return g
    c1=int(10) #count for easy level
    c2=int(5) #count for hard level
    level=input("do you want to play easy or hard?: ")
    c=int(0)
    d=int(0) #count
    if level=="easy":
        print("you are provide with 10 chance to guess the correct number")
        c=c1
    elif level=="hard":
        print("you are provide with 5 chance to guess the correct number")
        c=c2
    else:print("u entered something invalide..")
    d=c
    game_on=True
    while c>0 and game_on==True:
        if c>=1 and c<d:
            print(f"{c} chance remain... Give it a try again")
        g1=guess()
        if g1>a:
            print("to high...")
        elif g1<a:
            print("to low...")
        elif g1==a:
            print("you win!!")
            game_on=False
        else:print("u entered something invalide..")
        c-=1
        if c==0:
            print("u loss")
    contin=input("do u want to continue?(yes or no): ")
    if contin=="yes":
        import os
        os.system('cls')
    elif contin=="no":
        os.system('cls')
        print("thank you for visiting:)")
        cont=False