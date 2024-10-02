def media(a, b, c, d):
    resultado = (a + b + c + d) / 4
    return resultado

print('\n')

a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
c = float(input('Digite a terceira nota: '))
d = float(input('Digite a quarta nota: '))

print('\n')

resultado_media = media(a, b, c, d)

print(f'A sua média é {resultado_media:.1f}')

print('\n')

if resultado_media >= 7:
    print('Parabéns! Você teve um bom desempenho.')
else:
    print('Precisa melhorar.')

print('\n')