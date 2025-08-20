# ate 9 - mirim / ate 14 - infantil / ate 19 - junior / ate 25 - senior / acima - master
from datetime import date
ano = int(input('Informe o ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano
print ('<>' * 17)
print ('A confederação de natação informa:')
print ('O atleta está na categoria: ' ,end='')
if idade <= 9:
    print('MIRIM.')
elif idade <= 14:
    print('INFANTIL.')
elif idade <= 19:
    print('JUNIOR.')
elif idade <= 25:
    print('SÊNIOR.')
else:
    print('MASTER.')
print(f'Idade: {idade} anos.')
print ('<>' * 15)
