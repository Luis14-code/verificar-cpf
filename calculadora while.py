while True:
    numero1=int(input("escolha um numero:"))
    numero2=int(input("escolha outro numero:"))
    operador=input("escolhe seu operador +,-,*,/: ")

    if operador == "+":
     print(numero1+numero2)
    elif operador=="-":
       print(numero1-numero2)
    elif operador=="*":
       print(numero1*numero2)
    elif operador=="/":
       print(numero1/numero2)
    


    sair=input('quer sair? [s]im:').lower().startswith("s")
    
    if sair is True:
        break
