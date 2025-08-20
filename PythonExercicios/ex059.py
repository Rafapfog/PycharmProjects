# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar  # [ 2 ] multiplicar  # [ 3 ] maior  # [ 4 ] novos números  # [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sleep(0.5)
opçao = 0
while opçao != 5:
    print('''    [ 1 ] somar
    [ 2 ] Mulpiticlar
    [ 3 ] qual o número maior entre eles
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opçao = int(input('Qual é a sua opção: '))
    sleep(0.5)
    if opçao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {soma}.')
    elif opçao == 2:
        prod = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {prod}.')
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O valor maior entre {n1} e {n2} é {maior}.')
    elif opçao == 4:
        print('Informe os valores novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando programa.')
        sleep(1)
    else:
        print('Opção inválida, tente novamente.')
    print('=-_-=' * 10)
print('Fim do programa, volte sempre!!!')
