numeros = list(range(1, 11)) # inicia uma lista de 1 a 10

i = 0 # inicializa o índice em 0 

print("Números pares na lista:") 

while i < len(numeros): # a função while vai percorrer e verificar todos os elementos da lista
    if numeros[i] % 2 == 0: # verifica se o número atual na lista é par
        print(numeros[i])
    i += 1 # incrementa i em 1