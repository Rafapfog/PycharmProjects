# Curso Python #014 - Estrutura de repetição while
from time import sleep
'''for c in range(1, 11):
    print(c)
    sleep(0.5)
print('Fim')'''

'''c = 1
while c < 11:
    print(c)
    c += 1
    sleep(0.3)
print('FIM!!!')'''

n = 1
par = impar = 0
ntot = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        ntot += n
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
        print(f'a soma é {ntot}')
    print(f'Voce digitou {par} numeros pares e {impar} impares.')
print('Fim né!')
