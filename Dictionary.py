# Dictionary is a mutable datatype which is built and stores key value  pairs

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

first_dictionary = {'name':'Sasmit', 'age':26}
print(first_dictionary.values())
print(first_dictionary.keys())

second_dictionary = {'name':'Sasmit', 'age':26}
print(second_dictionary.values())

first_hash = hash('age')
second_hash = hash('age')
print(first_hash)
print(second_hash)

print(second_dictionary.items())
for key,value in second_dictionary.items():
    print(key)
    print(value)
    
#accessing elements in dictionary
name = second_dictionary['name']
print(name)

#accessing using get() method
name = second_dictionary.get('class')
print(name)

dict_1 = {'name':"abcd",'age':26}
dict_2 = {'age':26,'name':"abcd"}
print(id(dict_1))
print(id(dict_2))
print(dict_1==dict_2)
print(dict_1 is dict_2)

#mersing two dictionary

#1. union merge
result_dict = dict_1 | dict_2
print(result_dict)
print(id(result_dict))

#2. update merge
dict_1.update(dict_2)
print(dict_1)
print(id(dict_1))

# #3. intersection
# dict_1 = {'name':"abcd",'class':26}
# dict_2 = {'class':26,'name':"abcd"}
# result_dict = dict_1 & dict_2
# print(result_dict)

#4. keyword arguments merge
result_dict = {**dict_2,**dict_1}
print(result_dict)

#5. removing key value pair
dict_3 = {'name':'sasmit','age':22,'dom':'ddd'}
value = dict_3.pop('name')
print(value)
print(dict_3)

value = dict_3.popitem()
print(value)
print(dict_3)