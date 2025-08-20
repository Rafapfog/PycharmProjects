# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
# 2h = soma do quadrado dos catetos
# existem bibliotecas de modulos certos para resolução de calculos matematicos.\
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto advacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
hi = math.hypot(co, ca)
print(f'O valor da hipotenusa é: {hi:.2f}')