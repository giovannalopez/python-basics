import random

def gerar_numero():
    return random.randint(1, 50)

def jogar_jogo():
    numero = gerar_numero()
    tentativas = 0
    print('Eu pensei em um número entre 1 e 50. Tente adivinhar!')

    while True:
        tentativa = int(input('Sua tentativa: '))
        tentativas += 1

        if tentativa < numero:
            print('Número muito baixo! Tenta um número maior.')
        elif tentativa > numero:
            print('Número muito alto! Tenta um número menor.')
        else:
            print(f'Parabéns! Você acertou em {tentativas} tentativas.')
            break

    replay = input('Deseja jogar de novo? (s/n): ')
    if replay.lower().strip() == 's':
        jogar_jogo()
    else:
        print('Obrigado por jogar!')

jogar_jogo()