nome = str(input('Qual o seu nome? ')).strip()
upper = str.upper(nome)
print(f'Seu nome em letras maiúsculas é {upper}')
lower = str.lower(nome)
print(f'Seu nome em letras minúsculas é {lower}')
count = str.__len__(nome) - nome.count(' ')
print(f'Seu nome tem {count} letras')
find = nome.find(' ')
print(f'Seu primeiro nome tem {find} letras')