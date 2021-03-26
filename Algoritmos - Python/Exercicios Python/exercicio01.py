p1 = 1
p2 = 2
p3 = 3
p4 = 4
p5 = 5

5
n1 = int(input('Entre com nota 01='))
n2 = int(input('Entre com nota 02='))
n3 = int(input('Entre com nota 03='))
n4 = int(input('Entre com nota 04='))
n5 = int(input('Entre com nota 05='))

media_inicial = (p1*n1+p2*n2+p3*n3+p4*n4+p5*n5)
media_parcial = (p1+p2+p3+p4+p5)
media_final = media_inicial/media_parcial

print('media final = {}  '.format(media_final))
