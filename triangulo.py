lado1 = int(input("Digite : "))
lado2 = int(input("Digite : "))
lado3 = int(input("Digite : "))

if lado1 == lado2 and lado3 < lado1:
    print("É um Triângulo Isósceles")
    print("Existe dois lados iguais e um diferente.")
elif lado2 == lado3 and lado1 < lado2:
    print("É um Triângulo Isósceles")
    print("Existe dois lados iguais e um diferente.")
elif lado3 == lado1 and lado2 < lado1:
    print("É um Triângulo Isósceles")
    print("Existe dois lados iguas e um diferente.")
elif lado1 == lado2 and lado3:
    print("É um triângulo Equilátero")
    print("Todos os lados são iguais")
else:
    print("É um triangulo Escaleno")
    print("Todos os lados são diferentes")