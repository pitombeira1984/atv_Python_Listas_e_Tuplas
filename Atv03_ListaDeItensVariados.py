def ListaDeItensVariados():
    lista = []
    while True:
        item = input("Digite um item (ou 'sair' para encerrar): ")
        if item.lower() == 'sair':
            break
        lista.append(item)
    indice = int(input("Digite o indice do item que deseja selecionar: "))
    print(f'O indice  {indice} corresponde ao item: {lista[indice]}')
    return lista
print(ListaDeItensVariados())
