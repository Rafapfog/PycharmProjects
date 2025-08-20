# faça um programa que mostre:
# quantas vezes aparece a letra "A"
# em que posicao ela aparece a primeira vez
# em que posicao ela aparece a ultima vez
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes na frase {frase.capitalize()}')
print(f'A primeira letra apareceu na posicao {frase.find('A')+1}')
print(f'A ultima letra A aparece na posição {frase.rfind("A")+1}')
