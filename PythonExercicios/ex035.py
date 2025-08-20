# analise 3 numeros e diga se pode ser formado um triangulo:
import math
print('-=' * 15)
print('Analisador de Triangulos.')
print('-=' * 15)
a = float(input('Informe o primeiro segmento: '))
b = float(input('Inform o segundo segmento: '))
c = float(input('informe o terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR UM TRIANGULO!')
else:
    print("Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO.")