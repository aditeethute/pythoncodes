#day7
#HANGMAN project
#challenge 1 -choosing random word and with checking anwser
game_on=True
while game_on==True:
    print(" _ ")                                            
    print("| | ")                                            
    print("| |__    ___ _ __   __ _ _ __ ___   __ _ _ __")   
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ") 
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |") 
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|") 
    print("                    __/ |                      ") 
    print("                   |___/   ") 
    print("\n\n\n\nwellcome to the game of HANGMAN!!!,\nlet's check if you can guess the fantasy characters")
    stages=["  +----+\n       |\n       |\n       |\n       |\n       |\n=======+","  +----+\n  O    |\n       |\n       |\n       |\n       |\n=======+","  +----+\n  O    |\n /     |\n       |\n       |\n       |\n=======+","  +----+\n  O    |\n /|    |\n       |\n       |\n       |\n=======+","  +----+\n  O    |\n /|\   |\n       |\n       |\n       |\n=======+","  +----+\n  O    |\n /|\   |\n  |    |\n       |\n       |\n=======+","  +----+\n  O    |\n /|\   |\n  |    |\n /     |\n       |\n=======+","  +----+\n  O    |\n /|\   |\n  |    |\n / \   |\n       |\n=======+"]
    import random
    words=["marmaid","fae","dragon","fairy","vampire","werewolf","witches","wizard","king","queen","lord","lady","prince","princess","demon","devil","warrior","knight","highlord","highlady","giant","sorceress","warlock","shapeshifter","hag","ghost","assassin","deathwalker","maid","guardianangel","angle","enchanter","elf","rouge","monk","barbarian","ranger","kingsgaurd","commandar","pirate","seamonster","deathwalker",]
    chosen=random.choice(words) #randomly chosen word
    cl=list(chosen)            #cl-letters in chossen word as list
    display=cl
    game=False
    live=int(0) #count for the lives
    display=[]
    for l in range(len(cl)):
        display+="_"
    print(display)

    while not game:
        guess=input("guess the letter: ")
        #checking
        n=0
        for a in range(len(cl)):
            if cl[a]==guess:
                display[n]=guess
            n+=1
        print(display)
        if guess not in cl:
            print("you guess wrong and lose one life")
            print(stages[live])
            live+=1
        if "_" not in display:
            game=True
            print("you win!!!")
            
        if live==8:
            game=True
            print (chosen)
            print("you lose !!")
            
             
    yn=input("do you want to play again?(yes/no)*: ")   
    if yn=="no":
        print("thankyou for visiting.")
        game_on=False
    elif yn=="yes":
        import os
        os.system('cls')

