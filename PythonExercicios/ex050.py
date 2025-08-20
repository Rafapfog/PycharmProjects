#  prog que leia 6 numeros inteiros, e mostre a soma apenas dos que forem pares, se for impar, ignore!
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'indique um {c}º valor: '))
    if n % 2 == 0:
        soma += n
        cont = cont + 1
print(f'Você informou {cont} números PARES e a soma dos valores pares é igual a {soma}.')