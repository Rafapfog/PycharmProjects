# fazer um jogo que advinhe um numero entre 0 e 5 interativo que mostre um resultado de acordo se acertou ou nao.

import random
import time
print('Estou pensando em um número entre 0 e 5, vamos ver se você consegue advinhar!')
time.sleep(1)
num = int(input('em qual numero estou pensando? '))
print('Hummmm......')
time.sleep(1)
pc = random.randint(0, 5)
if num == pc:
    print(f'Parabens, você acertou!!!')
else:
    print("Errou, eu ganhei!")
time.sleep(1)
print(f'O número que eu pensei foi {pc}!')
