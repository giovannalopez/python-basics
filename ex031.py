distancia = float(input('Qual a distância da sua viagem? '))
print(f'Você irá fazer uma viagem de {distancia}Km')

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'O preço da sua passsagem será R${preço:.2f}')