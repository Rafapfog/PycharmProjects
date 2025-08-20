# desenvolva um programa que pergunte a distancia de uma viagem em km, e informe o valor da passagem
# por km (R$ 0,50 o km rodado), e acima de 200km, (R$0,45).
import time

viagem = int(input('Informe a distancia que deseja viajar: '))
print(f'Voce está preste a começar uma viagem de {viagem}Km.')
time.sleep(1)
if viagem < 201:
    print(f'O valor da passagem é R${viagem * 0.5:.2f}.')
else:
    print(f'O valor da viagem promocionalmente é de R${viagem * 0.45:.2f}.')
time.sleep(1)
print('Obrigado por cotar conosco!!!')