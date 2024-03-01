#day3.2 BMI2 exercise
#tell the user their BMI and their interpretation based on it
ht=float(input("please enter your height in m: "))
wt=float(input("please enter your weight in kg: "))
bmi=float(wt/ht**2)
if bmi<18.5:
    print(f"your BMI is {bmi}, it shows you are UNDERWEIGHT person.")
else:
    if bmi<25:
        print(f"your BMI is {bmi}, it shows you are a NORMAL WEIGHT person.")     
    else:
        if bmi<30:
          print(f"your BMI is {bmi}, it shows you are an OVERWEIGHT person.")
        else:
            if bmi<35:
              print(f"your BMI is {bmi}, it shows you are an OBESE person.")
            else:
                print(f"your BMI is {bmi}, it shows you are CLINICALLY OBESE person.")