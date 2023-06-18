idades_setor = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
                'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
                'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
                'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

medias_idades = {}
lista_idades = []
idades_elevadas = []
for setor, idade in idades_setor.items():
    # itera sobre os values calculando as médias e armazenando na lista_idades
    media = sum(idade) / len(idade)
    medias_idades[setor] = media
    lista_idades.extend(idade)

media_geral = sum(lista_idades) / len(lista_idades)  # Calcula a média dos setores

for idade in lista_idades:
    # itera sobre a lista_idades selecionando os valores acima da média_geral
    if idade > media_geral:
        idades_elevadas.append(idade)

for setor, idade in medias_idades.items():
    print(f"{setor}, idade média {idade:4.2f}")

print(f"A idade média geral é {media_geral:4.2f}")
print(f"Existem {len(idades_elevadas)} pessoas acima da idade média")
