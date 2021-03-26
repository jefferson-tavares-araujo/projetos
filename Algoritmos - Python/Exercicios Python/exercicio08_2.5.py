ano_nasc = int(input('Entre com ano de nascimento='))
ano_atual = int(input('Entre com ano atual='))

idade = ano_atual - ano_nasc

if idade >= 18 and idade >= 16:
    print('Sua idade é de {}, então você tem permissão de votar e tirar CNH'.format(idade))
elif idade < 18 and idade >= 16:
    print('Você tem {} anos, você poderá somente votar'.format(idade))
else:
    print('Você tem {} anos, nao pode votar ou tirar cnh'.format(idade))

