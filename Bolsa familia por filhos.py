SB = float(input("Entre com o valor do salario Bruto:"))
filhos = int(input("Entre com quantidade de filhos:"))
if filhos > 0:
    print("voce recebera 300 reais por filho")
else:
    print ("Não possui filhos")
auxilio=300.00
SF= filhos * auxilio
SL=(SB+SF)
print("O valor do salario liquido  é:" +str(SL))
 