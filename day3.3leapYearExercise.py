#day3.3
#to find if the entered year is a leap year
#a leap have 366 day,
#a leap year is evenly divisible by 4, EXCEPT if it's, UNLESS it have to be evenly divisible by 400
year=int(input("enter the year you want to check if it's leap: "))
if year%4==0:
    if year%100==0:
       if year%400==0:
        print(f"your entered year {year} is a leap year.") 
    else:
        print("your entered year {year} is not a leap year")    
else:
    print("your entered year {year} is not a leap year")
