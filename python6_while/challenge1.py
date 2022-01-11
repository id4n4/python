import random
count = 0
while True:
    count += 1
    roll = str(random.randint(1,5))
    num = input('Guess a number between 1 and 5: ')
    if roll == num:
        print(f'You guessed it in {count} tries!')
        break
