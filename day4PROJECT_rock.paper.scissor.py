#DAY4 PROJECT
#ROCK PAPER SCISSOR CODE
game=True
while game==True:
    import random
    rock="✊"
    paper="🖐"
    scissor="✌️"
    action=["✊","🖐","✌️"]
    user=int(input(print("hey there let's play rock, paper ,scissor!!.\nenter:\n 1 for rock,\n2 for paper,\n3 for scissor")))
    if user>3:
        print("you typed invalid number:|")
        exit()
    n=random.randint(0,2)
    comp=action[n]
    player=action[user-1]
    print(f"your choice: {player}\ncomputer's choice: {comp}")
    if player==comp:
        print("it's a tie!:|")
    elif player=="✌️" and comp=="🖐":  
        print("YOU WON!:)")    
    elif player=="🖐" and comp=="✊":
        print("YOU WON!:)")  
    elif player=="✊" and comp=="✌️":
        print("YOU WON!:)")  
    else:
        print("YOU LOSS!!:(")
    game_on=input("do you want to play again?(yes/no): ")
    if game_on=="no":
        game=False
        print("thank you for visiting.")


