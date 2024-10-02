from math import hypot
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hypot = hypot(co, ca)
print(f'A hipotenusa vai medir {hypot:.2f}')