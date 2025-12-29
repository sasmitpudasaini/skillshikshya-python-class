# 1.Arithmatic operators
#addition
a = 10
b = 20
c = a + b
print(c)

#substraction
a = 10
b = 20
c = a - b
print(c)


#multiplication
a = 10
b = 20
c = a * b
print(c)


#division
a = 10
b = 20
c = a / b
print(c)

#modulus division
a = 10
b = 20
c = a % b
print(c)

#floor division 
a = 10
b = 20
c = a // b
print(c)

#exponential operator
a = 10
b = 20
c = a ** b
print(c)


# 2. Relational operators

#equal to 
a = 10
b = 20
c = a==b
print(c)

#not equal to 
a = 10
b = 20
c = a != b
print(c)

#greater than 
a = 10
b = 20
c = a > b
print(c)

#smaller than 
a = 10
b = 20
c = a < b
print(c)

# 3. Logical operators
a = True
b = False
c = a and b
print(c)


a = True
b = False
c = a or b
print(c)


a = True
b = False
c =  not b
print(c)

#assignment operator
#with addition
a = 10
a += 20
print(a)

#with substraction
a = 10
a -= 20
print(a)

#with multipilcation
a = 10
a *= 20
print(a)

#with division
a = 10
a /= 20
print(a)

#with modular division
a = 10
a %= 20
print(a)

#with exxponential
a = 10
a **= 20
print(a)

#with float division
a = 10
a //= 20
print(a)

# Memnbership operators
a =[1,2,3,'hello',4]
b ="hello"
if b in a:
    print('true')
else:
    print('false')
    

#use in operator in dictionary keys or values to check membership
    
a ={'name':'sasmit','age':"22"}
b ="age"
if b in a.keys():
    print('true')
else:
    print('false')


# Bitwise operators
a = 2
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~b)