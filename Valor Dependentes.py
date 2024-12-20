VS = float(input("Entre com o valor do salario liquido"))
dependentes = int(input("Entre com quantidade de dependentes:"))
dependente = VS - 1200
VSTITULAR = VS - 300
if dependentes >= 1:
    
    print("O valor que o dependente vai pagar será:" +str(dependente))
else:
    
    print("O valor do salario liquido  é:" +str(VSTITULAR))
