#fazer um programa que divide os digitos de um numero: (centena, dezena, milhar... etc...)
import time
num = int(input('Informe um numero para ser analisado: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}...')
time.sleep(1)
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')


