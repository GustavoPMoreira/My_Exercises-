def DDD(ddd):
    Lista_ddd = {61: "Brasilia",
                71: "Salvador",
                11: "São Paulo",
                21: "Rio de Janeiro",
                32: "Juiz de Fora",
                19: "Campinas",
                27: "Vitoria",
                31: "Belo Horizonte"}
    for i in Lista_ddd:
        if ddd == i:
            return Lista_ddd[i]
    return "DDD não encontrado"
# main
if __name__ == "__main__":
    ddd = 32
    print(DDD(ddd))