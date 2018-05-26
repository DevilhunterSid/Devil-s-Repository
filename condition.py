a = 1
b = 2
print('\nVariables a is :', 'one' if ( a == 1) else 'Not one')
print('variable a is :', 'even' if (a % 2 == 0) else 'Odd')
print('\nVariable b is :', 'one' if (b == 1) else 'Not one')
print('variable b is :', 'even' if (b % 2 == 0) else 'Odd')
max = a if (a > b) else b
print('\nGreater Values is:', max)
