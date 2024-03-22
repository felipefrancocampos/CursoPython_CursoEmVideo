dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km foram rodados?'))

valor = (dias * 60) + (km * 0.15)

print('O valor a pagar pelo carro é de R${:.2f}'.format(valor))