#day5 project pypassword
game=True
while game==True:
    import random
    sym=["!","#","$","%","&","(",")","*","+"]
    num=["1","2","3","4","5","6","7","8","9","0"]
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    print("WELLCOME TO THE PASSWORLD GENERATOR!!\n")
    n_letter=int(input("how many letters do you want: "))#no of letters
    n_num=int(input("how many numerical you want: "))#no of numbers
    n_sym=int(input("how many symbols you want: "))#no of symbol
    password=""
    pass_ch=int(n_letter+n_num+n_sym)#total no of characters in password
    print(f"in total there are {pass_ch} characters in your password..")
    nl=0#count for no of letters
    nn=0#count for no of numbers
    ns=0#count for no of symbols
    for pc in range(1,100): #pc-password_characters
        n=int(random.randint(1,3)) #1-letter;2-num;3-syn
        length=len(password)
        if length<=pass_ch:
            if n==1 and nl<n_letter:
                ranl=int(random.randint(0,25))
                password+=letters[ranl]
                nl+=1
            elif n==2 and nn<n_num:
                rann=int(random.randint(0,9))
                password+=num[rann]
                nn+=1
            elif n==3 and ns<n_sym:
                rans=int(random.randint(0,8))
                password+=sym[rans]
                ns+=1
    print(f"generated password is {password}")
    # :| i could have choose random(list)..........AHHHHH.....but it work same hehe;)
    #actually its more easier..ahhhhhhhhhh.....
    character=["!","#","$","%","&","(",")","*","+","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    password=""
    for p in range(1,5):
        random.shuffle(character)
        ch=random.choice(character)
        password+=ch
    print(password)
    game_on=input("do you want to use it again?(yes/no): ")
    if game_on=="no":
        game=False
        print("thank you for visiting.")