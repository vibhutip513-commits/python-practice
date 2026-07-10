# Lists

# append()
# insert()
# remove()
# pop()
# sort()
# reverse()
# len()



# Practice
# Add 100 to a list.
# Remove 20 from a list.
# Sort a list in ascending order.
# Sort a list in descending order.
# Reverse a list.


# #1.
l=[1,2,4,5,6,7]
l.append(100)
print(l)

# #2.
l=[10,20,30,40,50]
l.remove(20)
print(l)

# 3,4,5
l=[12,34,21,35,678,766,3312,212]
l.sort()
l.reverse()
print(l)

#3.
l=[12,34,21,35,678,766,3312,212]
largest=l[0]
largest_list=[]
for i in l:
    if i>largest:
        largest=i
        largest_list.append(largest)
print(largest_list) 


