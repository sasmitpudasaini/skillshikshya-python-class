#forloop
#multiply each element by 2 and print the result
tuple1 = (0,1,2,3,4,5,6,7,8,9)
z=()
for i in tuple1: 
    z += (i*2,)
print(z)

#for loop
listing = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(listing)):
    listing[i] = listing[i] * 2
print(listing)

#for loop in one line
lsiting = tuple(i * 2 for i in listing)
print(type(listing))