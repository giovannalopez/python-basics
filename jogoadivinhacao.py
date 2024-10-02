import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou o número depois de {tentativas} tentativas.")
            break 
jogo_adivinhacao()