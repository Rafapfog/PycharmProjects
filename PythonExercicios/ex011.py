# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

l = float(input('digite a LARGURA da parede, em metros, a se pintar: '))
a = float(input('digite a ALTURA da parede, em metros, a se pintar: '))

print(f'Para uma parede de {l:.2f}m de largura, por {a:.2f}m de altura, sendo {l*a:.3f}m quadrados, precisaremos de {(l*a)/2:.1f} litros da tinta escolhida,\nvisto que cada litro de tinta, pintam 2 metros quadrados.')