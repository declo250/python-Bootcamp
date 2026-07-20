#Selecting random item from the list
import  random
friends = ["Alice","Bob","David","Tony","Henry"]

#first option
op1=random.choice(friends)
print(op1)
#second option
op2=random.randint(0,4)
choice=friends[op2]
print(choice)