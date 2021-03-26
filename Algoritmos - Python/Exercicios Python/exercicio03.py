
n=int(input("Digite um numero de 0 a 999 para saber quem e UNIDADE, DEZENA e CENTENA: "))
u=n // 1 % 10
d=n // 10 % 10
c=n // 100 % 10

print("unidade: ",u)
print("dezena: ", d)
print("centena: ", c)
