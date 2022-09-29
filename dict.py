empty_dict = {}
# declaring and initializing a dictionary
student_grades = {'Anna': 8, 'Edi': 10, 'George': 7, 'Ayana': 9, 'Mary': 8}
# where Anna is a key and 8 is a value

# how to print elements of the dictionary
print(student_grades)

# how to find values of different keys
print(student_grades['Ayana'])  # or
print(student_grades.get('Ayana'))

# how to update values
student_grades['Ayana']=10
print(student_grades)

# how to find out the length of a dictionary
print(len(student_grades))

# how to delete values
student_grades.pop('Anna')
print(student_grades)

# return only keys of a dictionary
print(student_grades.keys())
