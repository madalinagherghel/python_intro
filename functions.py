def print_greeting():
    print("Hello, you are welcomed ")


def greeting_by_name(name, surname):
    print(f'Hi {name}{surname}')


def nr_average(a, b, c):
    return (a+b+c)/3

# if person is above 18 can bet else not


def bet(age):
    if age>=18:
        print("You can bet")
    else:
        print("You cannot bet")


print_greeting()
greeting_by_name('Anderson', ' Maddie')
print(nr_average(4, 8, 7))
bet(int(input("Age is: ")))
