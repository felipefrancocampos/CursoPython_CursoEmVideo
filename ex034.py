salario = float(input('Qual o salário do funcionário? '))
if salario >= 1250:
    aumento = salario * 0.10
    novo = salario + aumento
    print('O aumento do salário foi de R${:.2f}'.format(aumento))
    print('Logo, o novo salário é R${:.2f}'.format(novo))
else:
    aumento = salario * 0.15
    novo = salario + aumento
    print('O aumento de salário foi de R${:.2f}, logo o salário total fica R${:.2f}'.format(aumento, novo))
