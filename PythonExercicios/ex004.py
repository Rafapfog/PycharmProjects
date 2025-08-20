# faça um programa que leia algo pelo teclado e mostre na tela o
# seu tipo primitivo e todas as informações possíveus sobre ele.

n = input("Escreva algo: ")
print(f"{n} - é letra?", n.isalpha())
print(f"{n} - é alfanumérico?", n.isalnum())
print(f"{n} - é numérico?", n.isnumeric())
print(f"{n} - é apenas ninusculo?", n.islower())
print(f"{n} - está em maiúsculo?", n.isupper())
print(f"{n} - é somente espaço?", n.isspace())
print(f"{n} - é imprimivel?", n.isprintable())
print(f"{n} - é capitalizado?", n.istitle())

print("Obrigado e tenha um ótimo dia!")
