from random import randint
from time import sleep

class JogoJokenpo:
    itens = ('Pedra', 'Papel', 'Tesoura')

    def __init__(self):
        self.jogador_escolha = None
        self.pc_escolha = None

    def mostrar_opcoes(self):
        print("\nVamos Jogar JOKENPÔ!")
        sleep(1)
        print('''Suas opções:
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')

    def obter_resultado(self):
        if self.jogador_escolha == self.pc_escolha:
            return "Empate!"
        elif (self.jogador_escolha == 0 and self.pc_escolha == 2) or \
             (self.jogador_escolha == 1 and self.pc_escolha == 0) or \
             (self.jogador_escolha == 2 and self.pc_escolha == 1):
            return "Você Ganhou!!! Parabéns!"
        else:
            return "Você Perdeu. Tente novamente!"

    def jogar(self):
        while True:
            self.mostrar_opcoes()
            try:
                escolha = int(input("Escolha sua jogada: "))
                if escolha not in [0, 1, 2]:
                    print("Entrada inválida! Escolha entre 0, 1 e 2. Reiniciando...\n")
                    sleep(1)
                    continue  # Reinicia o loop
            except ValueError:
                print("Por favor, insira um número válido. Reiniciando...\n")
                sleep(1)
                continue  # Reinicia o loop

            self.jogador_escolha = escolha
            self.pc_escolha = randint(0, 2)

            # Animação
            print("=-" * 15)
            for palavra in ["!JO", "KEN", "PÔ!"]:
                print(f"{' ' * (10 + len(palavra))}{palavra}")
                sleep(0.5)
            print("=-" * 15)

            # Resultado
            print(f"O computador escolheu {self.itens[self.pc_escolha]}.")
            print(f"Você jogou {self.itens[self.jogador_escolha]}")
            print(self.obter_resultado())
            break  # Encerra o jogo após um resultado válido

# Iniciar o jogo
JogoJokenpo().jogar()
