numero1 = float(input("Digite um número: ")) 
numero2 = float(input("Digite outro número: ")) 

condicao = "maior" if numero1 > numero2 else "menor" if numero1 < numero2 else "igual" 
#print "maior" se o número 1 for maior que o número 2.
#print "menor" se o número 1 for menor que o número 2.
#se os dois números forem iguais, print "igual".

print(f"O número {numero1} é {condicao} ao número {numero2}")