# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar  # [ 2 ] multiplicar  # [ 3 ] maior  # [ 4 ] novos números  # [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
opcao = 0
print('')
print('Tabela de opções, digite 2 números e escolha a opção que desejar.')
sleep(2)
n1 = int(input('Qual o primeiro numero: '))
n2 = int(input('Qual o segundo numero: '))
sleep(0.5)
while opcao != 7:
    print('''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Opções:
        [ 1 ] - Somar
        [ 2 ] - Subtrair
        [ 3 ] - Multiplicar
        [ 4 ] - Maior entre eles
        [ 5 ] - Menor entre eles
        [ 6 ] - Novos números
        [ 7 ] - Sair do programa
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*''')
    print('Qual a SUA opção?', end='')
    opcao = int(input(' = '))
    if opcao == 1:
        print(f'A Soma entre {n1} e {n2} é igual a {n1 + n2}.')
        sleep(3)
    elif opcao == 2:
        print(f'A subtração de {n1} menos {n2} é igual a {n1 - n2}.')
        sleep(3)
    elif opcao == 3:
        print(f'O produto de {n1} multiplicado por {n2} é igual a {n1 * n2}.')
        sleep(3)
    elif opcao == 4:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}.')
        sleep(3)
    elif opcao == 5:
        menor = 0
        if n1 < n2:
            menor = n1
        else:
            menor = n2
        print(f'O menor número entre {n1} e {n2} é {menor}.')
        sleep(3)
    elif opcao == 6:
        n1 = int(input('Qual o novo primeiro numero: '))
        n2 = int(input('Qual o novo segundo numero: '))
    elif opcao == 7:
        print('Desligando!', end='')
    else:
        print('Opção inválida, insira a opção correspondente abaixo:')
        sleep(3)
sleep(1)

sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end=' ')
sleep(1)
print('Até breve!')
sleep(2)
