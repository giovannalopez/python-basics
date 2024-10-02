medida = float(input('Digite uma medida: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
m = medida * 1
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m possui {km} em km\nA medida de {medida}m possui {hm} em hm\n'
      f'A medida de {medida}m possui {dam} em dam\n'
      f'A medida de {medida}m possui {cm} em cm\n'
      f'A medida de {medida}m possui {mm} em mm')