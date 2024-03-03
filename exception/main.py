val = input('Enter a number: ')
try:
    val = int(val)
    print(val)
except Exception:
    print('Something went wrong. Please try again.')
else:
    print('Everything went fine')
finally:
    print('Anything else?')

print('The program is still running')