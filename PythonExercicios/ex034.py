# escrever um prog que pergunte o salario de um funcionario e calcule o valor do seu aumento
# para salarios superiores a 1250, calcule um ameunto de 10%, para inferiores a isto, 15%.

sal = float(input('Informe o salário do funcionario: '))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)

print(f'Para o salário de {sal:.2f}, o novo salário será de R${novo:.2f}')