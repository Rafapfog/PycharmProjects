# escrever um prog. que leia a velocidade de um carro, se ele ultrapassar 80km;h, mostre uma mensagem de "multado"
# a multa vai custar R$7.00 por cada km acima do limite
import time
vel = float(input('Qual a velocidade atual do carro. '))
time.sleep(1)
if vel > 80:
    print('MULTADO, você excedeu o limite de velocidade de 80km!h!')
    print(f'Terá de págar uma multa de R${(vel-80) * 7:.2f}, pois é R$7.00 por km-h do limite!!!')

print('Tenha um bom dia! dirija com segurança!')
