from Q08 import Cidade, Estado

pb = Estado("Paraiba", "PB")
pb.adiciona_cidade(Cidade("Bonito de Santa", 12126))
pb.adiciona_cidade(Cidade("Sousa", 69997))
pb.adiciona_cidade(Cidade("Patos", 108192))
pb.adiciona_cidade(Cidade("Cajazeiras", 62576))

ce = Estado("Ceara", "Ce")
ce.adiciona_cidade(Cidade("Ipaumirim", 12473))
ce.adiciona_cidade(Cidade("Fortaleza", 2703391))
ce.adiciona_cidade(Cidade("Barro", 22758))
ce.adiciona_cidade(Cidade("Lavras da Mangabeira", 31508))

for estado in [pb, ce]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.população}")
    print(f"População do Estado: {estado.população()}\n")