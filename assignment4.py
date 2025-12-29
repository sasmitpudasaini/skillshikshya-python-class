# Assignment 4

# task 1
for i in range(1,51):
    print(i)
    if(i % 3 == 0 and i % 5 == 0):
        print("frizzbuzz")
    elif (i % 5 == 0):
        print("buzz")
    elif(i % 3 == 0):
        print("fizz")


#task 3

n=1234
while n > 0:
    num = n % 10
    print(num,end ='')
    n = n // 10

#task 4

# n = int(input("Enter any number: "))
# for i in range(2,n):
#     if(n % i == 0):
#         print("not prime")
#         break    