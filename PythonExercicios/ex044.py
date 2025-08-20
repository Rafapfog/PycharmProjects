from time import sleep
print('=' * 20)
print('{:=^20}'.format(' Lojas fogaça '))
preço = float(input('Preço das Compras: R$'))
sleep(0.5)
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista (dinheiro/cheque)
[ 2 ] à vista (cartão)
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
print('=' * 20)
opçao = int(input('Digite a opção desejada de pagamento: '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opçao == 4:
    total = preço * 1.2
    totparcel = int(input('Quantas parcelas: '))
    parcela = total / totparcel
    print(f'Sua compra será parcelada em {totparcel}x de R${parcela:.2f} COM JUROS.')
else:
    total = 0
    print('Opção INVALIDA de pagamento, informe novamente os dados!')
print(f'Sua compra é de R${preço:.2f}, e o valor final será de R${total:.2f} no final.')
