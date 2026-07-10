
## 1. Add 2 numbers
#"""sabse pehle function banaya usme perameter pass kiye then return kar ke sum operator ka use kiya then function call kiya or arguments pass kr diye"""
#def add(a,b):
#         return "sum=",a+b
# obj=add(19,23)
# print(obj)

# #2. square of a number: 
"""_summary_ subse pehle ek function banaya sqrt name se usme ek perameter pass kiya usko return kara diya or usme **2 ka multiply kiya taki uski power k according squrt return ho jaye
    """
# def sqrt(a):
#     return a**2

# obj=sqrt(a=int(input("Enter a number:")))
# print("Square of a number=",obj)




# #3. check if a number is even or odd
"""number 2 se divide ho kar reminder 0 dega to even nhi to odd simple code likh diya ,user input chaiye the to arrgument me comment pass kiya use input ka :user input lene ka or koi tareeka ho to batana
    """
# def even_odd(num):
#      if num%2==0:
#          return "Even"
#      else:
#          return "Odd"
     
# obj=even_odd(num=int(input("Enter a number:")))
# print(obj)


# #4.maximum of three numbers
"""isme math library use kar k max functioncall kar diya"""
# import math
# a=[12,34,23,45]
# def maximum():
#     return max(a)
# obj=maximum()
# print("Max=",obj)



#calculate factorial
""" factorial ka simple logic likh kar samjha ki fact 1 lenge or usme  ek ek kar ke number se chhota value multiplye karte jayege to vo aage badh raha he bahi kiya"""
# a=int(input("Enter a number:"))
# fact=1
# for i in range(1,a+1):
#     fact*=i
    
# print(fact)
   
# def factorial(a):
#   fact=1   
#   for i in range(1,a+1):
#         fact*=i
#   print(fact)
      
# f=factorial(4)
# # print("Factorial=",f)

#\\\\\SESSION 2\\\\\\
# def largest():
#     a=12
#     b=10
#     c=11
#     if a>b and a>c:
#         print(f"{a} is largest")
#     elif b>a and b>c:
#         print(f"{b} is largest")
#     else:
#         print(f"{c} is largest")

# largest()


# sum of list
# import math
# a=[12,23,34,12,45]
# print("sum=",sum(a))

# def Sum():
#     a=[12,23,34,12,45]
#     sum=0
#     for i in a:
#         sum+=i
#     print("Sum=",sum)
    
# Sum()
        
    



# def even_odd():
#     a=[12,15,20,33,40,51]
#     e_count=0
#     o_count=0
#     for i in a:
#         if i%2==0:
#             e_count+=1
#         else:
#             o_count+=1
#     print("Even Numbers: ",e_count)
#     print("Odd Numbers: ",o_count)
        
# even_odd()


##4. find the 2nd largest number
"""sabse pehle function banao usme jo list di he add kar do ab logic k liye traversing karege 
or if condition 
"""
# def Sec_Large():
#     a=[10, 50, 30, 90, 70]
  
#     a.sort()
#     print(a) 
#     print(a[-2])    
# Sec_Large()




# Question 1

# Find the smallest number in

# numbers = [12, 3, 45, 2, 9]

# Don't use

# min()
# sort()
# Question 2

# Count how many numbers are greater than 20.

# numbers = [12,34,45,6,89,2,56]

# Expected answer:

# 4



# #fIND THE SECOND LARGEST
# def sec_largest(num):
#     largest=num[0]
#     second=num[0]
#     for i in num:
#         if i>largest:
#             second=largest
#             largest=i
#         elif i>second and i!=largest:
#             second =i
#     return second
# num=[10,20,50,32,90,70]
# print("Second Largest= ",sec_largest(num))



def sec_smallest(num):
    smallest=num[0]
    second=num[0]
    for i in num:
        if i<smallest:
            second=smallest
            smallest=i
        elif i<second and i!=smallest:
            second=i
    return second

num=[1,2,3,4,5,6]
print("Second Smallest= ",sec_smallest(num))

# Count how many numbers are greater than 20.
def greater_then(numbers):
    greter=0
    for i in numbers:
        if i>20:
            greter+=1
    return greter
numbers = [12,34,45,6,89,2,56]
print(greater_then(numbers)," are greater then 20")

# 4


