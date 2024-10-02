def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'ERRO! Não é possível dividir por 0!'
    else:
        return a / b

print('Qual operação você irá utilizar?\n')
print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão \n')
escolha = input('Escolha uma opção. (1/2/3/4): ').strip()

print("\n")

a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))

if escolha == '1':
    resultado = adicao(a, b)
elif escolha == '2':
    resultado = subtracao(a, b)
elif escolha == '3':
    resultado = multiplicacao(a, b)
elif escolha == '4':
    resultado = divisao(a, b)
else:
    resultado = 'Operação inválida.'

print('\n')

print('Resultado:', resultado)

print('\n')