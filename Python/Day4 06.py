# Guess number
import random
answer = random.randint(1,20)
counter = 0
while True:
    counter +=1
    number = int(input('Please input answer:'))
    if number < answer:
        print('Bigger')
    elif number > answer:
        print('Smaller')
    else:
        print('You are right!')
        break
print('You use %f time' %counter)
if counter > 9:
    print('You are stupid')
elif counter < 4:
    print('You are lucky dog~')