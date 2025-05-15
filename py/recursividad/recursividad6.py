def aMayuscula(palabra):
    if not palabra:
        return ""
    
    return palabra[0].upper() + aMayuscula(palabra[1:])

palabra = "hola"
resultado = aMayuscula(palabra)
print(resultado)