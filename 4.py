def consonantes(cadena):
    cadena = cadena.lower()
    contador = 0
    for cad in cadena:
        if cad in "bcdfghjklmnpqrstvwxyz":
            contador += 1

    return contador

def main():
   cadena = "josueisraelreyesdiaz"
   print('Cadena: ',cadena)
   print('Cant. consonantes:',consonantes(cadena))


if __name__ == '__main__':
    main()
