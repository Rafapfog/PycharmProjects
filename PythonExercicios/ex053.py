# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# exemplos de palíndromos: apos a sopa, a sacada da casa, a torre da derrota, anotaram a data da maratona.
frase = str(input('digite uma frase: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo.')
print(f'Você digitou a frase: {junto}.')
print(f'o inverso é {inverso}')