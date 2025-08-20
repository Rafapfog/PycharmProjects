from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura') #   =   0. 1. 2
pc = randint(0, 2)
print('Vamos Jogar JOKENPÔ!')
sleep(1)
print('''Suas opções:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
sleep(1)
opcao = int(input('Escolha sua jogada: '))
if opcao >= 3:
    print('Escolha entre 0, 1 e 2 apenas. Tente novamente!')
else:
    print('=-' * 15)
    print('        JO')
    sleep(0.5)
    print('            KEN')
    sleep(0.5)
    print('                 PÔ!')
    print('=-' * 15)
    sleep(0.3)
    print(f'O computador escolheu {itens[pc]}.')
    print(f'Você Jogou {itens[opcao]}')
    print('=-' * 15)
    if pc == 0:  # PC JOGOU PEDRA
        if opcao == 0:
            print('Empatou!')
        elif opcao == 1:
            print('Você Ganhou!!! Parabéns!')
        elif opcao ==2:
            print('Você Perdeu. Tente novamente!')
    elif pc == 1: # PC JOGOU PAPEL
        if opcao == 0:
            print('Você Perdeu. Tente novamente!')
        elif opcao == 1:
            print('Empatou!')
        elif opcao == 2:
            print('Você Ganhou!!! Parabéns!')
    elif pc == 2: # PC JOGOU TESOURA
        if opcao == 0:
            print('Você Ganhou!!! Parabéns!')
        elif opcao == 1:
            print('Você Perdeu. Tente novamente!')
        elif opcao == 2:
            print('Empatou!')
