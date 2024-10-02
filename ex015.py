dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados: '))
pagar = (dias * 60) + (km * 0.15)
print(f'O valor a ser pago é {pagar:.2f}')