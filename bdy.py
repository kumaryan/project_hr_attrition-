

import time
from random import randint

for i in range(1,85):
    print('')
    print(YASMIN)

space = ''

for i in range(1,1000):
    count = randint(1, 100)
    while(count > 0):
        space += ' '
        count -= 1
    if(i%10==0):
        print(space + '๐Happy Birthday yasmin!')
    elif(i%9 == 0):
        print(space + "๐")
    elif(i%5==0):
        print(space +"๐")
    elif(i%8==0):
        print(space + "๐")
    elif(i%7==0):
        print(space + "๐ซ")
    elif(i%6==0):
        print(space + " Happy birthday yasmin๐")
    else:
        print(space + "๐ธ")

    space = ''
    time.sleep(0.2)
