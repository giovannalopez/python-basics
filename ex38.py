numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 > numero2:
    print(f"O número {numero1} é maior")
elif numero2 > numero1:
    print(f"O número {numero2} é maior")
else:
    print("Não existe valor maior pois os dois números digitados são iguais.")