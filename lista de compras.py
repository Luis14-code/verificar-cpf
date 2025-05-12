lista=[]
while True:
   
    ação1=input("[i] inserir , [r] retirar, [d] deletar, [s]sair: ")
    
    if ação1=="i":
        adicionar=input("oq deseja adicionar: ")
        lista.append(adicionar)
        print(lista)
    elif ação1=="r":
        retirar= input("qual produto voçê deseja retirar: ")
        lista.remove(retirar)
        print(lista)
    elif ação1 == "d":
        deletar = input("Deseja deletar toda a lista? (sim ou não): ")
        if deletar.lower() == "sim":
            lista.clear()
            print("Lista deletada.")
        print("Lista atual:", lista)
    elif ação1 == "s":
        print("Encerrando o programa.")
        break

        
