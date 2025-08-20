# crie um prog. que leia um numero inteiro e mostre na tela se ele é par ou impar.

import math
n = int(input('Informe um numero para saber se ele é par ou impar: '))
res = n % 2
if res == 0:
    print(f'O numero {n} é par!')
else:
    print(f'o numero {n} é impar!')