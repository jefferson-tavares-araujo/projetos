tanque_carro = int(input('Entre com a capacidade do tanque do carro = '))
litros = float(input('Entre com a quantidade de litros abastercidos = '))
km_corrido = float(input('Entre com KM percorrido antes do abastecimento = '))

diferenca = tanque_carro - litros
kmlitro = km_corrido / litros
kmrestante = diferenca * kmlitro

kilometragem = print('O veiculo percorrera %.2f km '% kmrestante)
print('O veiculo tem autonomia de %.2f km por litro' % kmlitro)