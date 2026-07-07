# #1.Hello World
# print("Hello world!")


# # 2.User Introduction
# name=input("Enter User name:")
# print(f"Hello {name}! Welcome to Python.")

# #3.ADD TWO NUMBERS
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# print("Sum=",a+b)

# #EVEN AND ODD
# integer=int(input("Enter a integer:"))
# if integer%2==0:
#     print("Even")
# else:
#     print("Odd")
    
    
# #LARGEST OF TWO NUMBERS
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# if a>b:
#     print(f"{a} is Large.")
# else:
#     print(f"{b} is large.")
    

# #SIMPLE CALCULATOR
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# operator=input("Operator")
# if operator=="+":
#     print("sum=",a+b)
# elif operator=="-":
#     print("Diff=",a-b)
# elif operator=="*":
#     print("Multiplication=",a*b)
# elif operator=="/":
#     print("Divition=",a/b)
# elif operator=="//":
#     print("Division=",a//b)
# elif operator=="%":
#     print("Modulo=",a%b)    

    
# #Multiplication Table
# num=int(input(""))


# #SUM OF FIRST N NUMBERS
# Method 1: Using loop
n = int(input("Enter n: "))
sum_total = 0
for i in range(1, n + 1):
    sum_total += i
print(f"Sum of first {n} numbers: {sum_total}")

# Method 2: Using formula (n*(n+1)/2)
# n = int(input("Enter n: "))
# sum_total = n * (n + 1) // 2
# print(f"Sum of first {n} numbers: {sum_total}")

# Method 3: Using built-in sum() function
# n = int(input("Enter n: "))
# sum_total = sum(range(1, n + 1))
# print(f"Sum of first {n} numbers: {sum_total}")
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")




# COUNT VOWELS
# Method 1: Using loop
word = input("Enter a word: ").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0
for char in word:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")

# Method 2: Using count() function
# word = input("Enter a word: ").lower()
# count = sum(word.count(vowel) for vowel in 'aeiou')
# print(f"Number of vowels: {count}")

# Method 3: Using list comprehension
# word = input("Enter a word: ").lower()
# count = len([char for char in word if char in 'aeiou'])
# print(f"Number of vowels: {count}")

# REVERSE A STRING
# Method 1: Using slicing
string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"Reversed string: {reversed_string}")

# Method 2: Using loop
# string = input("Enter a string: ")
# reversed_string = ""
# for char in string:
#     reversed_string = char + reversed_string
# print(f"Reversed string: {reversed_string}")

# Method 3: Using reversed() function
# string = input("Enter a string: ")
# reversed_string = "".join(reversed(string))
# print(f"Reversed string: {reversed_string}")

# Method 4: Using recursion
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return reverse_string(s[1:]) + s[0]
# 
# string = input("Enter a string: ")
# print(f"Reversed string: {reverse_string(string)}")