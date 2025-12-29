# num = [1,2,3,4,5]
# theirsum = 0
# for i in num:
#     theirsum = theirsum + i
# print(theirsum)

# Task 2: Find the Maximum and Minimum (Array Traversal)
# Goal: Understand how to keep track of state variables while looping through a list.
# The Problem:Given a list of numbers (e.g., [23, 45, 12, 56, 89, 3, 44]), write a loop to find the largest and smallest numbers in the list without using built-in functions like max() or min().
 
# Remarks: Please dont use the same method that we use in class.

#1.
# infinite_low_number = float('-inf')
# infinite_high_number = float('inf')
# n =[23, 45, 12, 56, 89, 3, 44]
# small = n[0]
# big = n[0]
# for i in n:
#     if i < small:
#         print("it is the smallest")
#     else:
#         small = n[0]
#         prin


#2.

listing = ['ram','shyam','hari','asmin','keshav']
for i in range(len(listing)):
    listing [i] =listing[i][::-1]
    print(i)

   


