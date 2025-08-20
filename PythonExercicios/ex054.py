# leia ano nasc de 7 pessoas, mostrar quantas ja atingiram a maioridade e quantos nao aringiram.
# Sendo 21 anos a maioridade.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
    else:
        totmenor +=1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade. Considerando a maioridade em 21 anos.')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade.')