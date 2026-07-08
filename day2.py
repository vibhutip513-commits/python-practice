# a=1
# while a<=100:
#     print(a)
#     a+=1


# a=100
# while a>=1:
#     print(a)
#     a-=1

# a=1
# while a<=100:
#     if a%2==0:
#         print(a)
#     a+=1

# a=1
# while a<=100:
#     if a%2!=0:
#         print(a)
#     a+=1

# a=5
# for i in range(1,11,1):
#     print(a*i)

#factorial
# num=4
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)
    
    
# import math
# num=int(input("Enter a number:"))
# result=math.factorial(num)
# print(result)

# n=int(input("Enter a number:"))
# for i in range(1,n+1,1):
#     print("*"*i)
  
# n=int(input("Enter a number:"))
# for i in range(n,0,-1):
#     print("*"*i)

# n=int(input("Enter a number:"))
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print(j, end=" ")
#     print(" ")
    
# n=int(input("Enter a number:"))
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print("*", end=" ")
#     print(" ")
  
# for i in range(n,0,-1):
#     for k in range(i-1,0,-1):
#         print("*", end=" ")
#     print(" ")


# #Decreasing Number Triangle
# n=int(input("Enter a number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print( )

#centred Pyrmind(Odd Stars)
rows=5
for i in range(rows):
    print(" "*(rows-i-1)+"*"*(2*i=1))