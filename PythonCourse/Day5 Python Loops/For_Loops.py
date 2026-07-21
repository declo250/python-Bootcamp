fruits =["Apple","Peach","Pear"]
for i in fruits:
    print(i)
student_sccore = [20,25,30,35,40,45,50,55,60,65,70,75,80,85,90 ,100]
#find maximum numbers using built in function
print(max(student_sccore))
#find total sum of the numbers in list using built function
total_score= sum(student_sccore)
#find total sum of the numbers in list using for loop
sums=0
for score in student_sccore:
    sums+=score
print(sums)
print(total_score)
#find maximum number in ist using for loop
max_value=0
for score2 in student_sccore:
    if score2 >max_value:
        max_value=score2
print(max_value)

#for loops and range function
#for number in range(a,b):
     #print(number)
for number in range(1,10):
    print(number)
#with steps
for number in range(1,10,3):
    print(number)
#sum of number in range of 1 to 100
sums3=0
for number in range(1,101):
    sums3+=number
print(sums3)
