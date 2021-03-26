dia_nasc = int(input("Dia Nascimento = "))
mes_nasc = int(input("Mes nascimento = "))
ano_nasc = int(input("Ano Nascimento = "))

dia_atual = int(input("Dia atual = "))
mes_atual = int(input("Mes atual = "))
ano_atual = int(input("Ano atual = "))

idade = ano_atual - ano_nasc
mes = mes_atual - mes_nasc
dia = dia_atual - dia_nasc


print("Você tem {} anos, {} meses e {} dias".format(idade,mes,dia))