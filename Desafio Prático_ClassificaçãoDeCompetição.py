def ClassificacaoMediaNotasCompeticao():
    resultados_equipe = [
        ("Natação", [9.8, 8.7, 9.2]),
        ("Futebol", [8.5, 9.1, 8.9]),
        ("Basquete", [9.6, 8.3, 9.5]),
        ("Vôlei", [7.8, 8.2, 7.9]),
        ("Atletismo", [8.4, 9.0, 8.6])
    ] 
    
    medias = []
    for nome, notas in resultados_equipe:
        media = sum(notas) / len(notas)
        medias.append((nome, media))    
    
    classificacao = sorted(medias, key=lambda x: x[1], reverse=True)   
   
    print("Classificação final das equipes:")
    for equipe, media in classificacao:
        print(f"{equipe}: {media:.2f}")

ClassificacaoMediaNotasCompeticao()

    