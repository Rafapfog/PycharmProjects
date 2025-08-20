import math
num =int(input('digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é igual a {raiz}')
print(f'A raiz quadrada de {num} arredondada para cima é igual a {math.ceil(raiz)}')
print(f'A raiz quadrada de {num} arredondada para baixo é igual a {math.floor(raiz)}')
