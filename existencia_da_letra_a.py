def verificar_letra_a(texto):
    contador = 0
    existe = False
    
    texto = texto.lower()
    
    for caractere in texto:
        if caractere == 'a':
            existe = True
            contador += 1

    if existe:
        if contador > 1:
            print(f"A letra 'a' ocorre {contador} vezes.")
        else:
            print(f"A letra 'a' ocorre {contador} vez.")
    else:
        print("A letra 'a' não ocorre no texto.")

texto = input("Digite um texto: ")
verificar_letra_a(texto)