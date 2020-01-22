print("\nBienvenido!")
print("\nEn este programa podras dar una solucion rapida y sencilla a las Ecuaciones cuadráticas por fórmula general.")

a =(float(input("\nPor favor ingrese el valor de A: ")))
b =(float(input("Por favor ingrese el valor de B: ")))
c =(float(input("Por favor ingrese el valor de C: ")))
import math
raiz = math.sqrt((b ** 2)-4*a*c)
x1= (-b + raiz)/(2*a)

x2= (-b - raiz) / (2*a)

print(f"x1= {x1:.2f}")
print(f"x2= {x2:.2f}")