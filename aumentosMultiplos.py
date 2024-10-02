salario = float(input("Qual o salário do funcionário?: "))
primeiroAumento = salario * (10 / 100)
segundoAumento = salario * (15 / 100)

novoSalarioPrimeiroAumento = salario + primeiroAumento
novoSalarioSegundoAumento = salario + segundoAumento

if salario > 1250:
    print(f"Quem ganhava {salario}, passa a ganhar {novoSalarioPrimeiroAumento:.2f}.")
else:
    print(f"Quem ganhava {salario}, passa a ganhar {novoSalarioSegundoAumento:.2f}")