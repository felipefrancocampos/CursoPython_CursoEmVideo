num = (int(input('Digite um número:')))
result = num % 2
print('O resultado foi {}'.format(result))

if result == 0:
    print('Você digitou um número par')
else:
    print('Você digiou um número ímpar')