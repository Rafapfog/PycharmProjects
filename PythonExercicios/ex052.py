#  prog que leia um numero inteiro e diga se ele é ou nao um numero primo.
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divizivel {tot} vezes.')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('Por isso ele não é primo!')