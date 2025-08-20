# faça um programa que diga se o ano é bissexto ou nao.
from datetime import date
ano = int(input('Informe o ano para saber se é bissexto. Deixe 0 (zero) para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
