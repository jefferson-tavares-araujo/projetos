a = int(input('Entre com um numero:'))
b = int(input('Entre com outro numero:'))
s = str(input('Entre com simbolo para calcular:'))

if s == '+':
    r = a + b
    print(' {} + {} = {}'.format(a,b,r))
elif s == '-':
    r = a - b
    print(' {} - {} = {}'.format(a,b,r))
elif s == '*':
    r = a * b
    print(' {} * {} = {}'.format(a,b,r))
elif s == '/':
    r = a / b
    print(' {} / {} = {}'.format(a,b,r))