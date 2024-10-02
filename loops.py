# WHILE: 
# i = 1

# while i < 10:
#    print(i)
#    i += 1

# print("pronto")
# print(i)


# FOR:
# nome = ["Giovanna", "Lopes", "dos Santos"]
# for item in nome:
#     print(item)

# amor = "Aninha"
# for letra in amor:
#     print(letra)

# print("Tabuada do 2:")
# for index in range(2, 21, 2): #Indica o ínicio, o fim e de quantos em quantos números vai pular.
#     print(index)

# for index in range(len(nome)):
#     print(nome[index], index)

# for index in range (0, 5):
#     if index == 0:
#         print("Primeira linha")
#     else:
#         print(f"Outras linhas {index}")


# FOR ANINHADO:
matriz_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for linha in matriz_numeros: 
    print("---")
    for coluna in linha:
        print(coluna)