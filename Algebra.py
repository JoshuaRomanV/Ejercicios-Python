import sys
print("\nBienvenido!")
print("\nEn este programa podras dar una solucion rapida y sencilla a las Ecuaciones cuadráticas por fórmula general.")
a = (float(input("\nPor favor ingrese el valor de A: ")))
if a == 0:
    print("Este no es un valor valido para A, compruebalo y vuelve a intentarlo :c.")
    sys.exit()
b = (float(input("Por favor ingrese el valor de B: ")))
if b == 0:
    print("Este no es un valor valido para B, compruebalo y vuelve a intentarlo :c.")
    sys.exit()
c = (float(input("Por favor ingrese el valor de C: ")))
if a == b and a == c:
    print("Error, no se pueden utilizar 3 valores identicos.")
    sys.exit()
import math
raiz = math.sqrt((b ** 2)-4*a*c)
x1 = (-b + raiz) / (2*a)
x2 = (-b - raiz) / (2*a)
print(f"x1= {x1:.2f}")
print(f"x2= {x2:.2f}")