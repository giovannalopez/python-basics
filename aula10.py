nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A sua média foi {media:.1f}')
if media >=6.0:
    print('Parabéns! Sua nota foi ótima.')
else:
    print('Precisa melhorar.')