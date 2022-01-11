import random
dice = random.randint(1,10)
cont = 0
num = 0
print('Guess a number between 1 and 10')
while dice != num:
    cont += 1
    num = input(f'Enter guess #{cont}: ')
    if num.isnumeric() == False:
        print('Numbers only, please!')
        continue
    num = int(num)
    if num > dice:
        print('Your guees is too high, try again!')
    elif num < dice:
        print('Your guees is too low, try again!')

    
else:
    print(f'You guessed it in {cont} tries!')
        