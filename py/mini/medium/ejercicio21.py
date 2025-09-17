"""Buscar palabras largas en un texto
Dado un texto, muestra solo las palabras que tengan más de 5 letras."""

with open('texto.txt','r',encoding='utf-8') as texto:
    for linea in texto:
        palabras = linea.strip().split()
        for palabra in palabras:
            if len(palabra.strip('!?,";')) > 5:
                print(f"la palabra: '{palabra}' tiene mas de 5 letras ") 
