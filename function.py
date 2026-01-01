
# #some built in function:
# for i in range(1,50):
#     print(i)

# a = [1,2,3,4]
# print(len(a))

# print(id(a))

# #greeting with function

# def greet_student(name):
#     print(f'hello, {name}!welcome to python class')
#     return f"Good day, {name}!"
# name = "Alice"
# result = greet_student(name)
# print(result)


# def greet_student(name,grade):
#     print (f"my name is {name}, {grade}")
#     return f"Good day, {name}!{grade}"
# print(greet_student('sasmit',5))

# #calculate the vo;ume of the cuboid
# def volume_cuboid(length=1,breadth=2,height=3):
#     return f"the volume of the cuboid is {length*breadth*height }"
    
# print(volume_cuboid())

# #print reverse using function
# def reverse_value(value):
#     return f"the volume of the cuboid is {value[::-1] }"

# print(reverse_value(value = [1,2,3]))

# #print a name multiple time

# def reverse_value():
#     z = (5)
#     k = "sasmit"
#     for i in range(1,z+1):
#         print(k)

# print(reverse_value())

# #recursive function
# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print (fibonacci(5))

# #sum of natural numbers using recursive function
# def sum_naturalnum(n):
#     if n==1:
#         return n 
#     else:
#         return n +sum_naturalnum(n-1)
    
# print (sum_naturalnum(5))

#from the list find the smallest number using the recursive function

# list=[1,2,3,4,5]
# def smallest(n):
#     if len(list)==1:
#         return list[0]
#     else:
#         small = smallest(list[1:])
# print()
            
#Wap to find palindrome using recursion

# def pali(n):
#     if n==n[::-1]:
#         return "it is palindrome"
#     else:
#         return "it is not palindrome"
    
# print(pali('1232'))
            
# #find leap year

# def leap_year(date):
#     if (date % 4 == 0 and date % 100 != 0) or (date % 400 == 0):
#         return ("the next leap year is ",date)
#     else:
#         return leap_year(date+1)
# print(leap_year(4))


# def lala(data):
#     if data == 1 :
#         return True
#     else:
#         return False
# print(lala(1))

#high order functions

# def add(x,y):
#     return(x+y)

# def subtract(x,y):
#     return(x+y)

# def multilpy(x,y):
#     return(x+y)
# def calculator(func,x,y):
#     return func(x,y)
# print(calculator((10,2)))

def highfunc(func):
    def insidefunc(*args, **kwargs):
        print(f"function{func.__name__} is called with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print (f"function {func.__name__} returned {result}")
        return result
    return insidefunc

@highfunc
def rev(s):
    return s[::-1]
s = 'sasmit'
print(rev(s))

def multiplier(factor):
    def multiply_by_factor(number):
        return number * factor
    return multiply_by_factor

multiplier_value = multiplier(5)
print(multiplier_value.__name__)
print(type(multiplier_value))
result = multiplier_value(10)
print(result)


#print if divisible by two using map function
def divtwo(num):
    return num%2 == 0 
numbers = [1,2,3,4,5]
result_data = map(divtwo,numbers)
print(list(result_data))


#convert the names into uppercase using map function
def case(num):
    return num.upper()
names = ['sasmit', 'ram' 'shhyam', 'hari']
result_data = map(case,names)
print(list(result_data))


#
def task(num):
        if sum(num)>10:
            return True
        else:
            return False
numbers = [[1,2,3], [4,5], [6,7,8,9]]
result_data = map(task,numbers)
print(list(result_data))

#using filter keep only even numbers
def is_even(num):
    return num % 2== 0
numbers =[1,2,3,4,5,6]

even_numbers = filter(is_even,numbers)
print(list(even_numbers))


#filter out the names which has words greater than 3
def is_even(num):
    if (len(num))<3:
        return (num)

numbers =['sasmit','ra','hall']

even_numbers = filter(is_even,numbers)
print(list(even_numbers))

# def dic(values):
#     if len(['name'])>5:
#         return values
# dict_3 = [
#     {'name':'sasmit','age':22},
#     {'name':'sasmit','age':22},
#     {'name':'sasmit','age':22}]

# dict_num = filter(dic,dict_3)
# print(list(dict_num))

#___ method 2---------#
# #sends filtering using dictionary into list 
data ={
    'name':'alisha',
    'name':'bishwaw',
    'name':'apple',
}
def name_length(item):
    return len(item['name'])>3

filter_data=filter(name_length,data)
print(dict(filter_data))

from functools import reduce
def max_num(x,y):
    if (x>y):
        return x
    else:
        return y

numbers = [1,2,3,4,5,5,6,67]
greatest_number = reduce(max_num,numbers)
print(greatest_number)
