
#indexing
a=[1,2,3,4]

print(a[0])

a=[1,2,3,4]

print(a[2])

a=[1,2,3,4]

print(a[-1])

a=[1,2,3,4]

#slicing
print(a[::-1])

#append method
a.append('end_item')
print(a)

#insert method
a.insert(1,"insert at 1")
print(a)

#print length
print(len(a))

#use insert method as append method
a.insert(6,"insert at 6")
print(a)

#mersing two lists
inner_list = [9,8,7]
print( a + inner_list)

#id of concatenated list
print(id(a))
print(id(inner_list))

#extend( it works as addition)
a.extend(inner_list)
print(a)
print(id(a))

#sort(its always in ascending order)
b=[1,3,5,2,4]
b.sort()
print(b)

#for dscending order
b.sort(reverse=True)
print(b)


#index
c =[2,3,4]
print(c.index(4))

#remove
c.remove(4)
print(c)

#pop
c.pop()
print(c)

