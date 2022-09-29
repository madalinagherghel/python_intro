# if - flow control
nice_song = True
rock_song = True
print('turn on the radio')
if nice_song is True and rock_song is True:
    print('level up')
    print('dance')
print('turn off radio')

# if else
# ex1 : if number is even print it
# else print odd
nr = 4
# even ? are exactly divisible by 2; nr%2=0
# odd  ? nr%2 != 0
if nr % 2 == 0:
    print('number is even')
else:
    print('number is odd')
# ex2 : number is positive? (number>0)
if nr > 0:
    print('number is positive')
else:
    print('number is not positive')

# if, else if , else
# ex1 how a robot say hi to us depending on what hour it is
hour = int(input('Hour is : '))
# input data from keyboard,and we assure that data is transformed from string to integer
if hour < 0:
    print('hour is negative, please enter a hour>0')
elif hour<=11:
    print('Good morning')
elif hour<=18:
    print('Good afternoon')
elif hour<=21:
    print('Good evening')
elif hour <=24:
    print('Good night')
else:
    print('Invalid hour. Hour is greater than 24')
    # tip:  if you want to select lines as a comment use CTRL+/
# ex 2 phone robot with options
option = int(input('choose an option '))
if option == 0:
    print('previous menu')
elif option == 1:
    print('you chose Ro language')
elif option == 2:
    print('you chose Eng language')
else:
    print('unidentified option, please try again')
