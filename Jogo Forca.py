palavra_secreta = ["A","D","I","D","A","S"]
letrasdescobertas = []
print("\n*** Jogo da Forca ***\n")
print("DICA: MARCA DE TENIS ")

for i in range(0,len(palavra_secreta)) :
    letrasdescobertas.append("-")
acertou = False
while acertou == False :
    letra = str(input("Digite a letra :"))

    for i in range(0, len(palavra_secreta)) :
        if letra == palavra_secreta[i] :
            letrasdescobertas[i] = letra
            print(letrasdescobertas[i])

    acertou = True
    for x in range(0,len(letrasdescobertas)):
        if letrasdescobertas [x] == "-" :
             acertou = False

print(palavra_secreta)


