rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
    if ival > 0:
        print('Nice work')
    else:
        print('Not a number')
except ValueError:
    print('Not a number')
