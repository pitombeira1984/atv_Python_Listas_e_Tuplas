def ProcurarNumero():
    numero_procurado = int(input("Digite o número a ser procurado: "))
    for i in range(1, 11):
        if i == numero_procurado:
            print(f"O número {numero_procurado} foi encontrado na posição {i}.")
            break
        else:
            print(f"O número {numero_procurado} não foi encontrado na posição {i}.")
            continue
ProcurarNumero()