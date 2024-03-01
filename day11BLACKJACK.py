#DAY11 PROJECT
#BLACKJACK

# sum should not more than 21 it's called BUST in this situation you lose , jack, queen, and king count as 10 ,ace as 1or11.if the dealer end up with a card sum less than 17 then they must take another card. tie is also called as push

import random
card=[2,3,4,5,6,7,8,9,10,10,10,10,11,]
def select():
    s_c=random.choice(card)
    if s_c==card[9] or s_c==card[11] or s_c==card[8] or s_c==card[10] :
        print("BLACKJACK♠︎ ♣︎ ♥︎ ♦︎!!!!")
    if s_c==card[12]:
        print("ACE")
    return s_c
def bust():
    n=user_cards[0]+user_cards[1]
    return n
def result():
    a=bust()+user_cards[2]
    b=dealer_check()
    c=bust()
    if c>21 or a>21:
        print("BUST!! you lose:(")
    elif a<b and a<21 and b<21:
        print("YOU LOSE!!:(")
    elif a==21 or a>b:
        print("YOU WIN!!")
    elif b==21:
        print("Dealer wins!!")
    elif a==b:
        print("AAHA! it's a TIE")
    elif b>21:
        print("DEALER BUST!! CONGRATS! you win..")
def dealer_check():
    d=comp_cards[0]+comp_cards[1]
    c=2
    while d<17:
        comp_cards.append(select())
        d+=comp_cards[c]
        print(f"new dealer's cards {comp_cards}")
        c+=1
    return d
game_on=True
while game_on==True:
    print("WELLCOME SIR/MADAM to game of BLACKJACK!! we are happy to have you here.")
    print("                     _")
    print("       ,'`.    _  _    /\    _(_)_")
    print("      (_,._)  ( `' )  <  >  (_)+(_)")
    print("        /\     `.,'    \/      |")
    print("                               _")
    print("       ,db.                  _(M)_")
    print("      (MMMM)       Stef     (M)+(M)")
    print("        db                     |")
    deal=input("do you want to deal?[yes OR no]: ").lower()
    print("loading $$$$ ")
    if deal=="yes":
        import os
        os.system('cls')
        user_cards=[]
        user_cards.append(select())
        user_cards.append(select())
        print(f"your cards {user_cards}")
        comp_cards=[]
        comp_cards.append(select())
        print(f"dealer cards {comp_cards},[$]")
        s2=input("do you want to hit(+) OR do you want to stand *[h OR s]*: ")
        if s2=="h":
            print("okay")
            user_cards.append(select())
            print(f"your new cards {user_cards}")
        if s2=="s":
            user_cards.append(0)
        bust()
        comp_cards.append(select())
        print(f"dealer cards {comp_cards}")
        result()
    elif deal=="no":
        print("thank you for visiting:)")
    else:print("you enter something invalide:|")
    game=input("ready for another deal? yes OR no?: ")
    if game=="no" or game=="yes":
        os.system('cls')
        if game=="no":
            game_on=False
            print("thank you for visiting")
    else: print("you enter something invalide:|")
    