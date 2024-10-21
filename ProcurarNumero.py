def numeroprocurado():
    numero_procurado = 7
    for i  in range(1, 11):
        if  i == numero_procurado:
            print(f"Número {numero_procurado} encontrado")
            break
        print(i)
numeroprocurado()
