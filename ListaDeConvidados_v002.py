def ListaDeConvidados():
    lista = ["Convidado1", "Convidado2", "Convidado3", "Convidado4", "Convidado5",
             "Convidado6", "Convidado7", "Convidado8", "Convidado9", "Convidado10"]
    convites = ["c01", "c02", "c03", "c04", "c05", "c06", "c07", "c08", "c09", "c10"]
    return lista, convites

# Obtenha a lista de convidados e convites
convidados, convites = ListaDeConvidados()

def ConsultarConvidadoPorConvite():
    convite = input("Digite o número do convite para consultar o convidado: ")
    if convite in convites:
        index = convites.index(convite)
        return convidados[index]
    else:
        return "Convite não encontrado."

# Exibir lista completa e consulta por convite
print("Lista de convidados:", convidados)
print("Lista de convites:", convites)

# Chamada da função de consulta
resultado = ConsultarConvidadoPorConvite()
print("Convidado encontrado:", resultado)



