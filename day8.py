# n=int(input("Enter how many times want to run the loop:"))
# for i in range(1,n+1,1):
#     print(i)


# n=int(input("Enter range:"))
# for i in range(1,n+1,1):
#     if i%2==0:
#         print(i)
        
        


# n=int(input("Enter range:"))
# for i in range(1,n+1,1):
#     if i%2==0:
#         print(i)


# n=int(input("Enter number:"))
# for i in range(1,11,1):
#   print(f"{n}*{i}={n*i}")


# n=int(input("Enter range:"))
# sum=0
# for i in range(1,n+1,1):
#     sum+=i
# print(sum)



# n=int(input("Enter number:"))
# fact=1
# for i in range(1,n+1,1):
#     fact*=i
# print(fact)



# n=int(input("Enter range:"))
# esum=osum=0
# for i in range(1,n+1,1):
#     if i%2==0:
#         esum+=i
#     elif i%2!=0:
#        osum+=i
    
# print(esum)
# print(osum)


# n=int(input("Enter a number:"))
# for i in range(1,n+1,1):
#     if n%i==0:
#         print(i)



# n=int(input("Enter a number:"))
# sum=0
# for i in range(1,n,1):
#     if n%i==0:
#         sum+=i
# print("sum=",sum)
# if sum==n:
#     print("Its Perfact number")
# else:
#     print("Its imperfact number")


# a=int(input("Enter a number:"))
# count=0
# for i in range(1,a+1):
#     if a%i==0:
#         count+=1

# if count==2:
#         print("Prime number")
# else:
#         print("Not prime")

# a=input("Write a string: ")
# b=''
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]
#     print(a[i])



# a=input("Write a string: ")
# b=''
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]
#     print(a[i])
    
# if b==a:
#     print("String is palindrom")
# else:
#     print("String is not a palindrom")



# str1="P@#yn26at^&i5ve"
# sym=0
# char=0
# num=0

# for i in str1:
#     if i.isdigit():
#         num+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         sym+=1
# print("leters=",char)
# print("Symbols=",sym)
# print("Numbers=",num)



# a=int(input("Enter a number:"))
# while a>0:
#    print(a%10)
#    a=a//10


# a=int(input("Enter a number:"))
# rev=0
# while a>0:
#     rev=rev*10+a%10
#     a=a//10
# print(rev)


# a=int(input("Enter a number:"))
# copy=a
# rev=0
# while a>0:
#     rev=rev*10+a%10
#     a=a//10
# #print(rev)
# if copy==rev:
#     print("a is palindrom")
# else:
#     print("a is not a palindrom")
    
    
import random

num=random.randint(1,10)
tries=0

while True:
    guess=int(input("Please guess your number b/w 1 to 10:"))

    if num==guess:
        tries+=1
        print(f"You are right,you guess the number in {tries} tries")
        break
        
    elif num<guess:
        print("Go a little lower")
        tries+=1
        
    elif num>guess:
        print("Go a little higher")
        tries+=1
    else:
        tries+=1
        print("You are wrong")