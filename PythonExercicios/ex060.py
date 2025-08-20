# progr para calcular fatorial:
from time import sleep
'''from math import factorial
num = int(input('Digite um número para calcularmos o seu Fatorial: '))
print(f'O fatorial do número {num} é {factorial(num)}')'''
n = int(input('Informe um número para calcular seu fatorial: '))
print('Calculando...')
sleep(0.5)
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')