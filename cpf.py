cpf = input("Digite seu CPF (somente números): ")
multiplicadores1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
multiplicadores2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

cpf = cpf[:9]  # pega os 9 primeiros dígitos

# Validação do tamanho
if len(cpf) != 9 or not cpf.isdigit():
    print("CPF inválido. Digite os 9 primeiros números.")
else:
    # Cálculo do 1º dígito verificador
    lista1 = []
    for i in range(9):
        numero = int(cpf[i])
        multiplicador = multiplicadores1[i]
        resultado = numero * multiplicador
        lista1.append(resultado)
        print(f"{numero} x {multiplicador} = {resultado}")
    
    soma1 = sum(lista1)
    conta1 = soma1 * 10
    resto1 = conta1 % 11
    if resto1 > 9:
        resto1 = 0
    print(f"Seu primeiro dígito verificador é: {resto1}")

    # Agora usamos os 9 dígitos originais + o 1º dígito para calcular o 2º dígito
    cpf_com_primeiro = cpf + str(resto1)

    # Cálculo do 2º dígito verificador
    lista2 = []
    for i in range(10):  # agora são 10 dígitos
        numero = int(cpf_com_primeiro[i])
        multiplicador = multiplicadores2[i]
        resultado = numero * multiplicador
        lista2.append(resultado)
        print(f"{numero} x {multiplicador} = {resultado}")

    soma2 = sum(lista2)
    conta2 = soma2 * 10
    resto2 = conta2 % 11
    if resto2 > 9:
        resto2 = 0
    print(f"Seu segundo dígito verificador é: {resto2}")

    # CPF completo
    cpf_final = cpf + str(resto1) + str(resto2)
    print(f"CPF completo com dígitos verificadores: {cpf_final}")
