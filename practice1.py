for i in range(1,51):
    print(i)
    
list = [23,45,12,56,89,3,44]
small = list[0]
big = list[0]
for i in list:
    if i < small:
        print('the minimum value is:' )
    else:
        small = list[0]
for j in list:
    if j < big:
        print('the maximum value is:')
    else:
        big = list[0]
    


