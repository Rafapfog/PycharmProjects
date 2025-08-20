#  Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerrará quando ele disser que quer mostrar 0 termos.
print('='*30)
print('SUPER PROGRESSAO ARITMETICÁ!')
print('='*30)
prim = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = prim
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while  cont <= total:
        print(f'{termo}', end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostradas.')
