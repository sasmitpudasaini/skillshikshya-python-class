#tuple

t1 = (1, 2, 3)
t2 = ("Python", 3.12, True)
print(t1)
print(t2)

#single element tuple (comma is mandatory)

single = (10,)
print(single)
print(type(single))

#without comma not a tuple

no_tuple = (10)
print(no_tuple)
print(type(no_tuple))

#Create a typle of ten element
tuple = (0,1,2,3,4,5,6,7,8,9)
print(tuple)

#print elements at multiple of 2

print(tuple[2::2])

#multiply each element by 2 and print the result
z=()
for i in tuple: 
    z += (i*2,)
print(z)

# list inside tuple
newtuple = (1,[1,2,3,4],3)
print(newtuple)

#changing the element of list inside tuple
newtuple[1][3] = 8
print(newtuple)


x = (1,2,[4,5,6],7)
print(x)
print(x[2])
x[2].insert(2, 0)
print(x)

#multiple indexing
data =((1,2), (3,4), (5,(1,2)))
print(data[2][1][1])

#flatten the tuple
data2 =((2,3),(2,3),(4,5))
# output (2,3,2,,3,4,5)

a = []
for i in data2:
    for j in i:
        a.append(j)
        
flatterned_tuple = tuple(a)
print(flatterned_tuple)
