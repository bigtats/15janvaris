def izlasit_teksta_failu(PD):
    with open(PD, 'r') as faila:
        faila_saturs = PD.read()
    print(faila_saturs)
faila_nosaukums = input("Ievadi faila nosaukumu (ar .txt paplašinājumu): ")
izlasit_teksta_failu(faila_nosaukums)