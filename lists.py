# in python lists can contain elements of different data types
# lists have dynamic dimension
fruits = ['apple', 'banana', 'orange', 3, True, 3]

# print a list
print(fruits)

# access an element by its index
print(fruits[3])

# add a new element
fruits.append('tomato')

# overwrite an element
fruits[1]='pear'
print(fruits)

# how to find out the length of a list
print(len(fruits))

# remove and return the last element of a list
last = fruits.pop()
print('the last element is: ', last)
print('the new list is: ', fruits)

# how many times an element appears
print('the element appear', fruits.count(3), 'times in the list')

# how to extend a list
exotic_fruits = ['mango', 'kiwi']
fruits.extend(exotic_fruits)
print(fruits)