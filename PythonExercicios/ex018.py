# faça um programa que leia um angulo qualquer e mostre na tela o valor do
# seno, cosseno e tangente desse angulo.
# existem bibliotecas de modulos certos para resolução de calculos matematicos.
import math
v = float(input('Informe o valor do angulo para saber seu seno, cosseno e tangente: '))
se = math.sin(math.radians(v))

co = math.cos(math.radians(v))

ta = math.tan(math.radians(v))
print(f'O angulo informado é {v:.0f}º, seu seno é {se:.2f}, seu cosseno {co:.2f} e sua tangente é {ta:.2f}.')
