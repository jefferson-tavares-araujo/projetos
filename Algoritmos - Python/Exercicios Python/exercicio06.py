valor_prestacao = int(input('Informe valor prestacao = '))
valor_atraso = (valor_prestacao +(valor_prestacao * 10)/100)
valor_final = (valor_prestacao - (valor_prestacao * 10)/100)

prejuizo = valor_prestacao - valor_final

print('O valor final com desconto a pagar será de =  {} reais'.format(valor_final))
print('Prejuizo de = {} reais'.format(prejuizo))