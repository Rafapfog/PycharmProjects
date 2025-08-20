# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
from random import randint
pc = randint(0, 10)
palpite = 0
print('Olá jogador, tente acertar qual valor estou pensando entre 0 e 5:')
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('mais... tente mais uma vez.')
        else:
            print('menos... tente mais uma vez.')
print('Acertou!!!')
print(f'Você fez {palpite} palpites!')
