#DAY14 PROJECT
############  HigherLower  ############# 
logo="""|+      |+                                           |+
|+      |+ __          |                             |+
|+______|+ OO          |                             |+
|+      |+  _   ,____, |___,  ,____, | /``)          |+       ,___,.      . ,____, | /``)
|+      |+ | | |     | |    | |____| |`  `   ++++++  |+       |   | \    /  |____| |`  `
|+      |+ |_| |_____| |    | |____. |               |+====== ,___,  \/\/   |____. |
                     |
                     |
               (,___,|
    """
print(logo)
import os 
import random
print("Wellcome to the game of HIGHER-LOWER!!\n(celebrites with higher number of follower)")
game=True
while game==True:
    p={"Virat Kohli":"162.49","Priyanka Chopra":"69.47","Shraddha Kapoor":"66.85","Neha Kakkar":"64.15","Narendraodi":"61.52","Deepika Padukone":"61.46","Alia Bhatt":"55.83","Jacqueline Fernandez":"55.75]","Akshay Kumar":"55.62","Katrina Kaif":"54.97","Anushka Sharma":"53.8","Sunny Leone":"48.48","Disha Patani":"46.95","Salman Khan":"45.73","Kriti Sanon":"44.06","Urvashi Rautela":"41.84","Hrithik Roshan":"38.36","Varun Dhawan":"38.16","Ranveer Singh":"36.75","Jannat Zubair":"36.09","Sara Ali Khan":"35.97","Mahendra Singh Dhoni":"35.82","Kapil Sharma":"35.14","Parineeti Chopra":"33.92","Nora Fatehi":"33.37","Sachin Tendulkar":"32.03","Tiger Shroff":"31.94","Sonam Kapoor":"31.51","Shahid Kapoor":"31.3","Guru Randhawa":"29.35","Amitabh Bachchan":"28.69","Madhuri Dixit":"27.43","Shah Rukh Khan":"26.77","anushka sen":"26.29","Avneet Kaur":"25.11","Mr Faisu":"24.14","Arishfa Khan":"23.62","Shreya Ghoshal":"22.95","Rashmikaandanna":"22.89","Shilpa Shetty":"22.7","Kartik Aaryan":"22.2","Riyaz Aly":"21.87","Rohit Sharma":"21.13","Kiara Advani":"20.84","Team India":"20.81","Sonakshi Sinha":"20.38","Ananya Pandey":"20.37","Kajal Aggarwal":"19.98","Mouni Roy":"19.76","Hardik Pandya":"19.63","Samantha Ruth Prabhu":"19.46","Taapsee Pannu":"19.26","Shruthi Haasan":"17.99","Suresh Raina":"17.93","Rakul Preet Singh":"17.75","Divyanka Tripathi Dahiya":"17.44","Filmy Gyan":"15.51","Sidharthalhotra":"15.21","Pooja Hegde":"15.06","Hina Khan":"14.85","Ayushmann Khurrana":"14.55","Tamanna Bhatia":"14.41","Yami Gautam":"14.1","Sonu Sood":"13.43","Ajey Nagar":"13.36","Malaika Arora":"13.33","Ileana D'Cruz":"13.15","Allu Arjun":"13","Vijay Deverakonda":"12.96","Janhvi Kapoor":"12.7","Neha Sharma":"12.36","Darshan Raval":"13.4","Arjun Kapoor":"12.03","Bhuvan Bam":"11.78","Diljit Dosanjh":"11.68","vraj Singh":"11.67","Hasnain Khan":"11.63","Ashish Chanchlani":"11.6","Kajol":"11.59","Sidhhi Agerwal":"11.44","Jennifer Winget":"11.39","Remo D'Souza":"11.26","Awez Darbar":"10.85","Karan Johar":"10.81","Garima Chaurasia":"10.71","KL Rahul":"10.66","Shaktiohan":"10.36","Keerthi Suresh":"10.3","Zareen Khan":"10.23","Shehnaaz Kaur Gill":"10.14","my Jackson":"10.11","Armaanalik":"10.09","Vicky Kaushal":"9.74","Himanshi Khurana":"9.61","Aishwarya Rai Bachchan":"9.55","naan Shaikh":"9.48","Siddharth Nigam":"9.41","Raghav Juyal":"9.4","Bipasha Basu":"9.3","John Abraham":"9.2"}
    def sec():
        n=random.choice(list(p.keys()))
        v=p[n]
        print(n)
        return n,v
    score=int(0)
    a=sec()
    print(a[1])
    b=sec()
    res=True
    while res==True:
        c=int(input("1st or 2nd (1/2)?: "))
        if c==1:
            if float(a[1])>float(b[1]):
                os.system('cls')
                score+=1
                print(f'your current score is:{score}')
                print(a[0],a[1])
                b=sec()
            else:
                res=False
        elif c==2:
            if float(b[1])>float(a[1]):
                score+=1
                os.system('cls')
                print(f'your current score is:{score}')
                print(b[0],b[1])
                a=b
                b=sec()
            else:
                res=False
        else:print("oops! you enter something invaild:|")
    def result():
        print(f"your score is {score}!")
        if score==0:
            print("we are really embarrased for you:|")
        elif score>=1 and score<3:
            print("is that even a score? you didn't reach the avegare score!\n let say this never happpen...")
        elif score>=3 and score<6:
            print("now that was somethimg ...\n give it a try again:) ")
        elif score>=6 and score<10:
            print("now that was the score to share... \n give it a try again score more than 10 and be in our top player.....;) ")
        else:
            print("that was legendary!!!!!")
    result()
    game_on=input("do you want to play again?(yes/no): ")
    if game_on=="no":
        game=False
        print("thank you for visiting:)")
    elif game_on=="yes":
        os.system('cls')



