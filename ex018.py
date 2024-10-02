import math
ang = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(ang))
print(f'O ângulo de {ang} tem o seno de {seno:.2f}')
cos = math.cos(math.radians(ang))
print(f'O ângulo de {ang} tem o cosseno de {cos:.2f} ')
tan = math.tan(math.radians(ang))
print(f'O ângulo de {ang} tem a tangente de {tan:.2f}')