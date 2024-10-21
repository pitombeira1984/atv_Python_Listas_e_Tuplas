def ListarVogais():
    vogais = []
    while len(vogais) < 5:
        IncluirVogais = input("Digite uma vogal: ").lower()
        if IncluirVogais in "aeiou":
            vogais.append(IncluirVogais)
        else:
            print("Digite apenas vogais!")
    return vogais
print(ListarVogais())
