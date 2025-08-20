# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# considere: US$1,00 = R$3,27

v = float(input("Digite o valor que possui para saber quantos dolares consegue comprar: R$"))
c = 3.27
print(f'Com o valor de R${v:.2f}, pode-se comprar US${v/c:.2f} dólares, à uma cotação de US${c}.')