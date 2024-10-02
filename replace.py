frase = input("Digite uma frase: ")
palavra_a_substituir = input("Digite a palavra que deseja substituir: ")
nova_palavra = input("Digite a nova palavra: ")

nova_frase = frase.replace(palavra_a_substituir, nova_palavra)

print(nova_frase)