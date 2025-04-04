import math 
import numpy 

def Menu():
    print("\n== Calculadora ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Bhaskara")
    print("6 - Definição de triangulos")
    print("7 - Porcentagem")
    print("8 - Regra de 3 simples")
    print("9 - Regra de 3 inversa")
    print("10 - Regra de 3 composta")
    print("11 - Conjuntos numéricos")
    print("0 - Sair")

def soma(a,b): 
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

def bhaskara(a,b,c):
    delta = b**2 - 4*a*c
    if delta <= 0:
        print("A conta não tem resultados reais")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"R: x1 = {x1} e x2 = {x2}")

def CalcTri(a,b,c):
    if (a != b != c):
        print("Triangulo escaleno")
    elif(a==b!=c or b==c!=a or a==c!=b):
        print("Triangulo isósceles")
    elif (a==b==c):
        print("Triangulo equilátero")

Menu()
while True:
    opcao = int(input("Escolha a operação: "))

    if opcao == 0:
        print("Saindo")
        break

    elif opcao == 1:
        a = float(input("Digite o valor A: "))
        b = float(input("Digite o valor B: "))
        print(f"R: {soma(a, b)}")
    elif opcao == 2:
        a = float(input("Digite o valor A: "))
        b = float(input("Digite o valor B: "))
        print(f"R: {subtracao(a, b)}")
    elif opcao == 3:
        a = float(input("Digite o valor A: "))
        b = float(input("Digite o valor B: "))
        print(f"R: {multiplicacao(a, b)}")
    elif opcao == 4:
        a = float(input("Digite o valor A: "))
        b = float(input("Digite o valor B: "))
        print(f"R: {divisao(a, b)}")
    elif opcao == 5:
        a = float(input("Digite o valor A: "))
        b = float(input("Digite o valor B: "))
        c = float(input("Digite o valor C: "))
        bhaskara(a, b, c)
    elif opcao == 6:
        a = float(input("Digite o valor A: "))
        b = float(input("Digite o valor B: "))
        c = float(input("Digite o valor C: "))
        CalcTri(a, b, c)
    elif opcao == 7:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        R = (a / 100) * b
        print(f"R: {a}% de {b} é igual a {R}")
    elif opcao == 8:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        c = float(input("Digite o valor de C: "))
        X = b * c / a
        print(f"R: {X}")
    elif opcao == 9:
        a1 = float(input("Digite o valor de A: "))
        b1 = float(input("Digite o valor de B: "))
        a2 = float(input("Digite o valor de C: "))
        b2 = (a1 * b1) / a2
        print(f"R: {b2}")
    elif opcao == 10:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        c = float(input("Digite o valor de C: "))
        d = float(input("Digite o valor de D: "))
        e = float(input("Digite o valor de E: "))
        R = a * (b / c) * (e / d)
        print(f"R: {R}")
    elif opcao == 11:
        resp = ""
        cj1 = set()
        cj2 = set()
        cj3 = set()

        while resp != 'exit':
            cj1.add(int(input("Insira um valor para o primeiro conjunto: ")))
            resp = input("Deseja encerrar? (exit): ")
            print(cj1)

        resp = ""

        while resp != 'exit':
            cj2.add(int(input("Insira um valor para o segundo conjunto: ")))
            resp = input("Deseja encerrar? (exit): ")
            print(cj2)
            
        resp = ""
        
        if input("Deseja inserir um valor no terceiro conjunto?: (Sim/Não) ") != 'Sim':
                break
        cj3.add(int(input("Insira um valor para o terceiro conjunto: ")))
        resp = input("Deseja encerrar? (exit): ")
        print(cj3)

        print("União:", cj1 | cj2 | cj3)
        print("Interseção:", cj1 & cj2 & cj3)
        print("Diferença:", cj1 - cj2 - cj3)
        print("Diferença Simétrica:", cj1 ^ cj2 ^ cj3)
        prodcart = [(a, b, c) for a in cj1 for b in cj2 for c in cj3]
        print("Produto Cartesiano:", prodcart)

    else:
        print("Opção inválida!")
