palavra = str(input("Digite uma palavra: "))

if palavra == palavra[::-1]:
    print(f"A palavra {palavra} é palíndroma.")
else:
    print(f"A palavra {palavra} não é palíndroma.")