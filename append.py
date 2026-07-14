#Question 1 Take 5 numbers from the user and store them in a list.
a=[]
for i in range(5):
    num=int(input("Enter Numbers:"))
    a.append(num)
print(a)

#Question 2 Store only the even numbers in a new list.
b=[1,23,4,3,45,56,67,678,787,232]
even=[]
for i in b:
    if i%2==0:
      even.append(i)
print(even)
        
# Question 3 Store only the odd numbers in another list.
b=[1,23,4,3,45,56,67,678,787,232]
odd=[]
for i in b:
    if i%2!=0:
      odd.append(i)
print(odd)

# Question 4 Take 5 names from the user and store them in a list.
name=[]
# name.append("Vibhuti")
# name.append("Divya")
# name.append("Deeksha")
# name.append("Rani")
# name.append("Surendra")

for i in range(5):
    n=input("Enter name:")
    name.append(n)


print(name)

# Question 5 Create a list of squares.
a=[1,2,3,4,5]
square=[]
for i in a:
    c=i**2
    square.append(c)
print(square)