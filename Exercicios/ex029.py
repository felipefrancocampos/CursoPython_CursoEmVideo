vel = float(input('Qual é a velocidade atual do carro?'))
if vel > 80:
    print('MULTADO!')
    multa = (vel-80) * 7
    print('Você deve pagar R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

