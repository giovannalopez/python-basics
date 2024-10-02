larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem {larg}x{alt} e sua área é de {area}m²')
print(f'Serão necessários {tinta}L de tinta para pintar essa parede.')