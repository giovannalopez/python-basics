import random
i1 = str(input('Primeiro item: '))
i2 = str(input('Segundo item: '))
i3 = str(input('Terceiro item: '))
i4 = str(input('Quarto item: '))
lista = [i1, i2, i3, i4]
random.shuffle(lista)
print('A ordem de compras será ')
print(lista)