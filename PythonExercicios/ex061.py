# refazer ex051 = só que usando WHILE:
print('='*30)
print('PROGRESSAO ARITMETICÁ!')
print('='*30)
prim = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = prim
cont = 1
while  cont <= 10:
    print(f'{termo}', end=' -> ')
    termo += razao
    cont += 1
print('ACABOU!')
