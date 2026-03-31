import random
import time

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida_max = vida
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        dano = random.randint(10, self.ataque)
        time.sleep(1)
        alvo.vida -= dano
        print(f"{self.nome} causou {dano} de dano em {alvo.nome}")

    def regenerar(self):
        cura = int(self.vida_max * 0.5)
        self.vida += cura

        if self.vida > self.vida_max:
            self.vida = self.vida_max

        print(f"{self.nome} regenerou {cura} de vida!")

    def mostrar_vida(self):
        print(f"{self.nome}: {self.vida}/{self.vida_max} HP")


def criar_inimigo(nivel):
    vida = 80 + (nivel * 20)
    ataque = 15 + (nivel * 5)
    return Personagem(f"Goblin Lv{nivel}", vida, ataque)


jogador = Personagem("Herói", 100, 20)

nivel = 1
inimigo = criar_inimigo(nivel)


while jogador.vida > 0:
    print(f"\n--- Batalha contra {inimigo.nome} ---")

    while inimigo.vida > 0 and jogador.vida > 0:
        # 🔥 MOSTRAR VIDA AQUI (CORRETO)
        print("\n--- STATUS ---")
        jogador.mostrar_vida()
        inimigo.mostrar_vida()

        print("\n1 - Atacar")
        escolha = input("Escolha: ")

        if escolha == "1":
            jogador.atacar(inimigo)
        else:
            continue

        if inimigo.vida <= 0:
            print(f"{inimigo.nome} foi derrotado!")

            jogador.regenerar()

            nivel += 1
            inimigo = criar_inimigo(nivel)

            break

        inimigo.atacar(jogador)

        if jogador.vida <= 0:
            print("Você morreu...")
            break