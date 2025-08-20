# desenvolver prog que leia o primeiro termo e a razao de uma PA (progreção aritmetica),
# no final, mostre os 10 primeiros termos dessa progressao.
print('='*30)
print('PROGRESSAO ARITMETICÁ!')
print('='*30)
prim = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = prim + (10 - 1) * razao
for c in range(prim, decimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU!')