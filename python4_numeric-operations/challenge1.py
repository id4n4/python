grades = input('What is the temperature in fahrenheit? ')

if grades.isnumeric() == False:
    print('Input is not a int number')
    exit()

grades = int(grades)

celsius = int((grades - 32) * (5 / 9))

print(f'Temperature in celsius is {celsius}')