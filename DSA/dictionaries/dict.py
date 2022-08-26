# using curly braces
mydict = {'name': 'John', 'age': 30}
print(mydict)

# accessing elements through keys
print(mydict['name'])
print(mydict['age'])

# Using Dictionary Comprehensions
Dict = {x: x**2 for x in [1,2,3,4,5]}
print(Dict)

# Dictionary Comprehensions with if condition
Dict = {x: x**2 for x in [1,2,3,4,5] if x%2==0}
print(Dict)

# Using Zip function to create a dictionary
list1 = ['a','b','c']
list2 = [1,2,3]
dict = {k:v for (k,v) in zip(list1, list2)}
print(dict)