# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = soma = quant = media = maior = menor = 0
opcao = 'S'
while opcao in 'Ss':
    num: int = int(input('Informe um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
media = soma / quant
print(f'a soma dos números é {soma} e a média é {media}.')
print(f'O maior foi o {maior} enquanto o menor foi o {menor}.')
