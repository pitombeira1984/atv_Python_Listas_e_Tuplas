def EncontrarNumeroPrimo():
    for numero in range(1, 20):
        if numero > 1:
            for i in range(2, numero):
                if (numero % i) == 0:
                    break
            else:
                print(f'{numero} é  um número primo!')

EncontrarNumeroPrimo()