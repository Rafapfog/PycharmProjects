# faça um algoritmo que lea o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('informe o valor do produto que ganhará o desconto de 5%: R$'))
# p = valor do produto
d = p-(p*5/100)
# d = desconto de 5% aplicado
print(f'O produto X, que está no valor de R${p:.2f}, com 5% de desconto, ficará R${d:.2f}.')