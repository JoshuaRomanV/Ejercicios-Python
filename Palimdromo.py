palindromo = 1
if palindromo == str(palindromo):
    palindro = palindromo.casefold()
else:
    print("valor no reconocido")
    exit()

revez = reversed(palindromo)
if list(palindromo) == list(revez):
        print("Es un palindromo! :) ")
else:
      print("No es un palindromo :( ")






