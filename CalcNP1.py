import math 

def Menu():
    print("\n== Calculadora ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Bhaskara")
    print("6 - Definição de triangulos")
    print("7 - Porcentagem")
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
     opcao = int(input("Escolha a operação"))
     
     if opcao ==0:
         print("Saindo")
         break
     
     elif opcao == 1:
         a = float(input("Digite o valor A"))
         b = float(input("Digite o valor B"))
         print (f"R: {soma(a,b)}")
     elif opcao == 2:
         a = float(input("Digite o valor A"))
         b = float(input("Digite o valor B"))
         print (f"R: {subtracao(a,b)}")
     elif opcao == 3:
         a= float(input("Digite o valor A"))
         b= float(input("Digite o valor B"))
         print (f"R: {multiplicacao(a,b)}")
     elif opcao == 4:
         a= float(input("Digite o valor A"))
         b= float(input("Digite o valor B")) 
         print (f"R:{divisao(a,b)}")   
     elif opcao == 5:
         a= float(input("Digite o valor A"))
         b= float(input("Digite o valor B"))
         c= float(input("Digite o valor C"))   
         bhaskara(a,b,c)
     elif opcao == 6:
         a= float(input("Digite o valor A"))
         b= float(input("Digite o valor B"))
         c= float(input("Digite o valor C"))   
         CalcTri(a,b,c)
     elif opcao == 7:
         a= float (input("Digite o valor de A"))
         b= float (input("Digite o valor de B"))
         R=(a /100) *b
         print(f"R:{a} % de {b} e igual a {R}")
     else:
         print("Não e possível")
    
     
