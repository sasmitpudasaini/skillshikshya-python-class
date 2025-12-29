
#some built in function:
for i in range(1,50):
    print(i)

a = [1,2,3,4]
print(len(a))

print(id(a))

#greeting with function

def greet_student(name):
    print(f'hello, {name}!welcome to python class')
    return f"Good day, {name}!"
name = "Alice"
result = greet_student(name)
print(result)


def greet_student(name,grade):
    print (f"my name is {name}, {grade}")
    return f"Good day, {name}!{grade}"
print(greet_student('sasmit',5))

#calculate the vo;ume of the cuboid
def volume_cuboid(length=1,breadth=2,height=3):
    return f"the volume of the cuboid is {length*breadth*height }"
    
print(volume_cuboid())

#print reverse using function
def reverse_value(value):
    return f"the volume of the cuboid is {value[::-1] }"

print(reverse_value(value = [1,2,3]))

#print a name multiple time

def reverse_value():
    z = (5)
    k = "sasmit"
    for i in range(1,z+1):
        print(k)

print(reverse_value())

#recursive function
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print (fibonacci(5))

#sum of natural numbers using recursive function
def sum_naturalnum(n):
    if n==1:
        return n 
    else:
        return n +sum_naturalnum(n-1)
    
print (sum_naturalnum(5))

#from the list find the smallest number using the recursive function

# list=[1,2,3,4,5]
# def smallest(n):
#     if len(list)==1:
#         return list[0]
#     else:
#         small = smallest(list[1:])
# print()
            
#Wap to find palindrome using recursion

def pali(n):
    if n==n[::-1]:
        return "it is palindrome"
    else:
        return "it is not palindrome"
    
print(pali('1232'))
            
#find leap year

def leap_year(date):
    if (date % 4 == 0 and date % 100 != 0) or (date % 400 == 0):
        return ("the next leap year is ",date)
    else:
        return leap_year(date+1)
print(leap_year(4))


def lala(data):
    if data == 1 :
        return True
    else:
        return False
print(lala(1))

