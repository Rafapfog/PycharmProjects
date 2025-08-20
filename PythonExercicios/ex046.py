# contagem regressiva de 10 a 0 com meio segundo de demora entre os numeros pra estouro de fogos.

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('Bum Bum POWW.')
