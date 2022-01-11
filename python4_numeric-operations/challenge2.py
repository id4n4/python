print('Simple calculator!')
first_number = input('First number? ')
operation = input('Operation? ')
second_number = input('Second number? ')

if first_number.isnumeric() == False or second_number.isnumeric() == False:
    print('Please input a number')
    exit()


first_number = int(first_number)
second_number = int(second_number)

if operation == '+':
    result = first_number + second_number
    label = 'sum'
elif operation == '-':
    result = first_number - second_number
    label = 'difference'
elif operation == '*':
    result = first_number * second_number
    label = 'product'
elif operation == '/':
    result = first_number / second_number
    label = 'quotient'
elif operation == '%':
    result = first_number % second_number
    label = 'modulus'
elif operation == '**':
    result = first_number ** second_number
    label = 'exponent'
else:
    print('Operation not recognized.')
    exit()

print(f'The {label} of {first_number} {operation} {second_number} equals {result}')
