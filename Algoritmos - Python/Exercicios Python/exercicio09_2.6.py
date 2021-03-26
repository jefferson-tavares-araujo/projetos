codigo = int(input('Entre com codigo do produto='))

if codigo == 1:
    print('Alimento nao perecivel')
elif codigo == 2 or codigo == 3 or codigo == 4:
    print('Alimento perecivel')
elif codigo == 5 or codigo == 6:
    print('Vestuario')
elif codigo == 7:
    print('Higiene Pessoal')
elif codigo >=8 and codigo <=15:
    print('Limpeza e utensilios domesticos')
else:
    print('Codigo invalido')