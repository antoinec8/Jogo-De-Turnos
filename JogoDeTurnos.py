import random

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
    
    def ataque_normal(self, alvo):
        dano = random.randint(self.get_nivel() * 3, self.get_nivel() * 6)
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano.")
    
    def ultimate(self, alvo):
        dano = random.randint(self.get_nivel() * 7, self.get_nivel() * 10)
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} com a ultimate {self.get_ultimate()} e causou {dano} de dano.")

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, ultimate):
        super().__init__(nome, vida, nivel)
        self.__ultimate = ultimate

    def get_ultimate(self):
        return self.__ultimate

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nUltimate: {self.get_ultimate()}\n"

class Vilao(Personagem):
    def __init__(self, nome, vida, nivel, ultimate):
        super().__init__(nome, vida, nivel)
        self.__ultimate = ultimate

    def get_ultimate(self):
        return self.__ultimate

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nUltimate: {self.get_ultimate()}\n"

class Jogo:
    def __init__(self):
        self.heroi = Heroi("Ashe", 1000, 18, "Flecha de Cristal Encantada")
        self.vilao = Vilao("Kaisa", 1200, 18, "Instito Assasino")

    def iniciar_combate(self):
        print(f"Iniciando a batalha!")
        while self.heroi.get_vida() > 0 and self.vilao.get_vida() > 0:
            print(f"\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.vilao.exibir_detalhes())
            print()
            escolha = input(f"Escolha: 1 - Ataque Normal, 2 - Ultimate: ")
            if escolha == "1":
                self.heroi.ataque_normal(self.vilao)
            elif escolha == "2":
                self.heroi.ultimate(self.vilao)
            else:
                print("escolha errada")

            if self.vilao.get_vida() > 0:
                escolha_vilao = random.randint(1, 2)
                if escolha_vilao == 1:
                    self.vilao.ataque_normal(self.heroi)
                else:
                    self.vilao.ultimate(self.heroi)
            
        if self.heroi.get_vida() > 0:
            print(f"\nParabéns, {self.heroi.get_nome()}!")
            print(f"Você venceu a batalha!")
        else:
            print(f"\nVocê foi derrotado!")
            print(f"{self.vilao.get_nome()} venceu a batalha!")

jogo = Jogo()
jogo.iniciar_combate()