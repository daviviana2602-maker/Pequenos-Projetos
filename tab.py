while True:
    try:
        tab = int(input('enter the number (positive) and the program gives the mutiplication table for you: '))
        if tab < 0:
            print('enter the valid number (positive number)')
        else:
            print('-' * 20)
            print(f'{tab} * 1 = {tab * 1}')
            print(f'{tab} * 2 = {tab * 2}')
            print(f'{tab} * 3 = {tab * 3}')
            print(f'{tab} * 4 = {tab * 4}')
            print(f'{tab} * 5 = {tab * 5}')
            print(f'{tab} * 6 = {tab * 6}')
            print(f'{tab} * 7 = {tab * 7}')
            print(f'{tab} * 8 = {tab * 8}')
            print(f'{tab} * 9 = {tab * 9}')
            print(f'{tab} * 10 = {tab * 10}')
            print('-' * 20)
            repeat = input('you want insert other number? (yes/no): ').strip()
            if repeat.lower() == 'yes':
                continue
            else:
                break
    except ValueError:
        print('invalid input, please enter a valid positive integer number')