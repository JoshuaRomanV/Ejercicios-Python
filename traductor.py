import goslate
print("Hola bienvenido!\n")
print("Traductor español-ingles\n")
palabra = input("Ingrese la palabra que desea Traducir al ingles:")
Tr = goslate.Goslate()
print(Tr.translate(palabra, 'en'))
