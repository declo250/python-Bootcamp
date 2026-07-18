weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.85:
    print("Underweight")
elif bmi >=18:
    print("Normal weight")
elif bmi >= 25:
    print("Overweight")
