valor = float(input('Entre com o valor do produto='))
codigo = int(input('Entre com o codigo do produto='))

if codigo == 1:
    desconto = valor * 0.1
    valor_final = valor - desconto
    print('Seu produto custara = {}'.format(valor_final))
elif codigo == 2:
    desconto = valor * 0.05
    valor_final = valor - desconto
    print('Seu produto custara = {}'.format(valor_final))
elif codigo == 3:
    parcela = valor / 2
    print('Seu produto custara 2 parcelas de = {}'.format(parcela))
elif codigo == 4:
    acrescimo = valor * 0.1
    valor_final = valor + acrescimo
    valor_dividido = valor_final / 3
    print('Seu produto tera acrescimo de 10% custara = {}'.format(valor_final))
    print('3 parcelas de = {}'.format(valor_dividido))
else:
    print('Codigo invalido')

