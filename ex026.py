frase = str(input('Digite uma frase: ')).upper().strip()
count = frase.count('A')
print(f'A letra A aparece {count} vezes na frase')
find = frase.find('A') + 1
print(f'A primeira letra A apareceu na posição {find}')
rfind = frase.rfind('A') + 1
print(f'A última letra A apareceu na posição {rfind}')