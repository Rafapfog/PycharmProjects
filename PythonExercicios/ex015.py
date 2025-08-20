#escreva um programa que pgerunte a quantidade de Km percorrido por um carro aligado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 po Km rodado.

d = int(input('Digite quantos dias ficou com o carro alugado: '))
km = float(input('Informe quantos Km foram rodados: Km '))
vd = d*60
vkm = km*0.15
vt=vd+vkm
print(f'O valor total do aluguel ficou em R${vt:.2f}')