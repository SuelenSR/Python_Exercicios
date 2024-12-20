altura = float (input('Digite a sua altura: '))
sexo = input('Digite o seu sexo: F - Feminino   M - Masculino ')
peso = float (input('Digite seu peso: '))
if sexo == 'F' or sexo == 'f':
    peso_ideal = (62.1*altura) - 44.7
    print("O peso ideal é %.0f"%(peso_ideal))
    if peso > peso_ideal:
        print('Você está acima do peso ideal')
    elif peso < peso_ideal:
        print('Você está abaixo do peso ideal')
    else:
        print('Você está dentro do peso ideal')   
else:
    peso_ideal = (72.7*altura) - 58
    print("O peso ideal é %.0f"%(peso_ideal))
    if peso > peso_ideal:
        print('Você está acima do peso ideal')
    elif peso < peso_ideal:
        print('Você está abaixo do peso ideal')
    else:
        print('Você está dentro do peso ideal')