texto = ("josueisraelreyesdiaz").lower()

vocales = ('a', 'e', 'i', 'o', 'u')

for letra in vocales:
    texto = texto.replace(letra, "")
texto = texto
print (texto)
