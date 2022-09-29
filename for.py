# print 101 dalmatians
for i in range(1, 101):
    print(f'Dalmatian number {i} ')

# print 101 dalmatians with a step of 2
for i in range(1, 101, 2):
    print(f'Dalmatian number {i} ')

# traversing an array by index
numbers=[3, 7, 10, 15, 25]
for i in range(0, len(numbers)):
    print(f'current index is {i}')
    print(f'current number is {numbers[i]}')
# for each
s=0
for number in numbers:
    s=s+number
print(f'Sum is {s}')