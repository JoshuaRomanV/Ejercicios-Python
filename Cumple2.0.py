import calendar
import sys
print("\nBienvenido!")
print("\nEn este programa podras saber que dia de la semana sera tu cumpleaños c:")
d = int(input("\nPor favor ingrese su dia de nacimiento:  "))
if d > 1 and d<31:
    dia = d
else:
    print("No es un dia valido, por favor confirmelo y vuelva a intentarlo :c")
    sys.exit()
m = int(input("Por favor ingrese su mes de nacimiento(En numeros): "))
if m > 1 or m < 12:
    mes = m
else:
    print("No es un mes valido, por favor confirmelo y vuelva a intentarlo :c")
    sys.exit()
a = int(input("Por favor ingrese el año en el que quiera saber que dia cae su cumpleaños:"))
if a > 1:
    año = a
else:
    print("No es un año valido, por favor confirmelo y vuelva a intentarlo")
    sys.exit()
if mes == 2 and dia == 29 and año % 4 != 0:
    print("\nOye que inusual que cumplas años ese dia, este año no tienes cumpleaños :c.")
else:
    day = calendar.weekday(año,mes,dia)
    days = ["Lunes.", "martes.", "Miercoles.", "Jueves.", "Viernes.", "Sabado.", "domingo."]
    print(f"\nFelicidades, tu cumpleaños en ese año sera el dia {days[day]}")




