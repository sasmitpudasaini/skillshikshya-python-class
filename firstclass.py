#value = 10
#print(value)
#print(id(value))
#vakueprint(type(value))

a="sasmit"
b="hello"

value = a.upper()
print(value)

second_value = a.lower()
print(second_value)

third_value = a.title()
print(third_value)

fourth_value = a.startswith('s')
print(fourth_value)

fifth_value = a.endswith('t')
print(fifth_value)

sixth_value = a.strip()
print(sixth_value)

message = 'hello'
iterator = iter(message)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#print(message[5])

a=-10
print(id(a))

a = "sasmit pudasaini"
print( "a[0:6] =", a[0:6])
print( "a[:6] =", a[-1::])
print('length of text=', len(a))

for char in "CAT":
    print(char)