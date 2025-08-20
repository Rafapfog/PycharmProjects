from time import sleep
print('Olá, hoje iremos verificar se os segmentos podem formar um triangulo e qual é ele.')
sleep (1)
a = float(input('Informe o primeiro segmento: '))
b = float(input('Informe o segundo segmento: '))
c = float(input('informe o terceiro segmento: '))
# equilatero - todos lados iguais / isosceles - dois lados iguais / escaleno - todos lados diferentes:
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triangulo ', end='')
    if a == b == c:
        print('Equilátero.')
    elif a == b != c or a == c != b or b == c != a:
        print('Isósceles.')
    elif a != b != c != a:
        print('Escaleno!')
else:
    print("Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO.")
