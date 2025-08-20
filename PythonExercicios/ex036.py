# escrever um programa para aprovar um emprestimo bancario para a compra de uma casa.
# Pergunte o valor da casa, o salario do comprador, e em quantos anos ele vai pagar.
# a prestação mensal nao pode ultrapassar 30% do salario ou entao o emprestimo sera negado.
casa = float(input('Valor da casa: R$ '))
salario = float(input('Valor do salário: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos:.0f} anos ', end='')
print(f'a prestação será de R${prestacao:.2f}.')
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')