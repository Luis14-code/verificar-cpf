import os
palavra_secreta = "perfume" 
letras_acertadas=""
numero_tentativas= 0

while True : 
    letras_digitadas = input("digite uma letra")
    numero_tentativas +=1

    if len(letras_digitadas)>1:
        print("digite apenas uma letra")
        continue

    if letras_digitadas in palavra_secreta:
        letras_acertadas += letras_digitadas

    palavra_formada= " "
    for letra_secreta in palavra_secreta:
        letras_acertadas += letras_digitadas
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada+=letra_secreta
        else:
            palavra_formada += '*'
    print('palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
     os.system('clear')
     print('voce ganhou')
     print('a palavra era', palavra_secreta)
     print('voce ganhou', numero_tentativas)
     letras_acertadas=" "
     numero_tentativas= 0