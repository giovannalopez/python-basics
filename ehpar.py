def ehPar(numero):
    if (numero % 2 == 0):
        return "par"
    else:
        return "ímpar"

numero = int(input("Digite um número inteiro: "))
resultado = ehPar(numero)
print(f"O número {numero} é {resultado}.")