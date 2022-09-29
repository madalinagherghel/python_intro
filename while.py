# exercise : the car run till it runs out of gasoline
gasoline_liters = 10
while gasoline_liters>0:
    print('accelerate')
    gasoline_liters=gasoline_liters-1
    if gasoline_liters <=3:
        print('warning! You have less than 3 L')
print('Stop!')