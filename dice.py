import random 

while True:
    print('1.roll the dice  2. exit')
    user= int(input("what you want to do\n"))
    if user ==1:
        number = random.randint(1,6)
        print("your dice number is ", + number)
    else:
        break    