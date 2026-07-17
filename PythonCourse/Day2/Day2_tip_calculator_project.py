print("Welcome to the tip calculator")
total = float(input("What was the total?$ "))
tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
person=int(input("How many people to split the bill?"))
total_tip=(total*tip)/100
sum2= (total_tip +total)/person
sum3=round(sum2,2)
print(f"Each person should pay: ${sum3}")