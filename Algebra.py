a = int(input("Por favor ingrese el valor de: A"))
b = int(input("Por favor ingrese el valor de: B"))
c = int(input("Por favor ingrese el valor de: C"))
import math
raiz = math.sqrt((b ^ 2)-4*a*c)

x1= (-b + raiz) / 2*a

x2= (-b - raiz) / 2*a

print(f"x1={x1}")
print(f"x2={x2}")