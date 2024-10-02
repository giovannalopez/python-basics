anoNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

idade = anoAtual - anoNascimento
tempoRestante = 18 - idade
atrasoDeAnos = idade - 18

if idade == 18:
    print(f"Você tem {idade} anos, está na hora de se alistar ao serviço militar.")
elif idade > 18:
    print(f"Se você ainda não se alistou, está {atrasoDeAnos} anos atrasado para o alistamento militar.")
else:
    print(f"Você tem {idade} anos, menores de idade não podem se alistar ao serviço militar. Faltam {tempoRestante} anos para a sua maioridade e para o seu alistamento.")
