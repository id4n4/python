while True:
    print('Would you like to continue?')
    result = input()
    if result == "no" or result == 'n':
        print('exiting')
        break
    elif result == 'y' or result == 'yes':
        print('Continuing ...')
        print('Complete!')
        break
    else:
        print('Please try again and respond with yes or no.')