def ListaDeConvidados():
    lista = []
    while True:
        nome = input("Digite o nome do convidado (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        convite = input("Digite o convite do convidado: ")
        dados = (nome, convite)  
        lista.append(dados)  
    return lista

convidados = ListaDeConvidados()

def PesquisarConvidado():
    nome = input("Digite o nome do convidado a ser pesquisado: ")
    for convidado in convidados:
        if convidado[0] == nome:
            return convidado[1]
    return "Convidado não encontrado"

# Chamada da função de pesquisa
resultado = PesquisarConvidado()
print(resultado)
