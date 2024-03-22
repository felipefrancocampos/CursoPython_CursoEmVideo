print('Olá, tudo bem? Vou te ajudar a calcular quanto tu deves comprar de tinta para a sua parede!')

largura = int(input('Qual a largura?'))
altura = int(input(' Qual a altura?'))

result = largura * altura  / 2

print("Você deve comprar {} litros de tinta".format(result))