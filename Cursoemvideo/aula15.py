'''cont = 1
while cont <= 10:
    print(cont, '-> ',end='')
    cont += 1
print('Acabou')'''
nome = 'jose'
idade = 21
sal = 1234.4
print(f'O {nome:-^10} tem {idade} anos e um salário de {sal:.2f}.')
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')