def celsius_fahrenheit(c):
    return (c * 9/5 + 32)

def fahrenheit_celsius(f):
    return (f - 32) * 5/9

def celsius_kelvin(c):
    return (c + 273.15)

def kelvin_celsius(k):
    return (k - 273.15)

def kelvin_fahrenheit(k):
    return ((k - 273.15) * 9/5 + 32)

def fahrenheit_kelvin(f):
    return ((f - 32) * 5/9 + 273.15)

def converter_temperatura():
    print("\nBem-Vindo(a) ao ConverteTemper!")
    print("Qual conversão de temperatura você gostaria de fazer? ")
    print("\n(1) Celsius para fahrenheit")
    print("(2) Fahrenheit para celsius")
    print("(3) Celsius para kelvin")
    print("(4) Kelvin para celsius")
    print("(5) Kelvin para fahrenheit")
    print("(6) Fahrenheit para kelvin\n")

    escolha = int(input("Escolha e digite o número da opção desejada: "))

    if escolha == 1:
        celsius = float(input("Digite a temperatura em celsius: "))
        print(f"A temperatura em celsius convertida para fahrenheit é {celsius_fahrenheit(celsius):.2f}°F.\n")
    elif escolha == 2:
        fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
        print(f"A temperatura em fahrenheit convertida para celsius é {fahrenheit_celsius(fahrenheit):.2f}°C.\n")
    elif escolha == 3:
        celsius = float(input("Digite a temperatura em celsius: "))
        print(f"A tempertatura em celsius convertida para kelvin é {celsius_kelvin(celsius):.2f}K.\n")
    elif escolha == 4:
        kelvin = float(input("Digite a temperatura em kelvin: "))
        print(f"A temperatura em kelvin convertida para celsius é {kelvin_celsius(kelvin):.2f}°C.\n")
    elif escolha == 5:
        kelvin = float(input("Digite a temperatura em kelvin: "))
        print(f"A temperatura em kelvin convertida para fahrenheit é {kelvin_fahrenheit(kelvin):.2f}°F.\n")
    elif escolha == 6:
        fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
        print(f"A temperatura em fahrenheit convertida para kelvin é {fahrenheit_kelvin(fahrenheit):.2f}K.\n")
    else:
        print("Opção inválida! Tente novamente.")

converter_temperatura()