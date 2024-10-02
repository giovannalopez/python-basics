valor  = float(input('Qual o preço do produto? '))
novo = valor - (valor * 5 / 100)
print(f'O produto que custava R${valor}, com 20% de desconto custará R${novo:.2f}')