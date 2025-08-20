# refaça o desafio 9 (tabuada), de um numero que o usuario escolher, so que agora utilizando um laço 'for'
t = int(input("Digite um número para sabermos sua tabuada: "))
for c in range(1, 11):
    print(f"{c} x {t:2} = {c*t}")
