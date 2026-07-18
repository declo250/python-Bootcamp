print("Welcome to rollercoaster!")
height= int(input("what is your height in cm? "))
bill=0
age = int(input("What is your age?"))
if height >=120:
    print("You can ride the rollercoaster")
    if age <=12:
        bill=5
        print(f"child ticket is {bill}")

    elif age <=18:
       bill=7
       print(f"Youth ticket si {bill}")
    elif age >=45 and age<= 55:
        print("Have Free ticket")
    else:
      bill=12
      print(f"Adult ticket is {bill}")
    photo=input("Do you need photo? Type Yes or No? ")
    if photo =="yes":
        bill+=3
        print(f"Your final bill is {bill}")

else:
    print("You can not ride the rollercoaster")
