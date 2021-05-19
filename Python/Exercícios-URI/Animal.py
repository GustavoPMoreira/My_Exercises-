def vertebrado(e2,e3):
    if e2=="ave":
        if e3=="carnivoro":
            print("aguia")
        elif e3=="onivoro":
            print("pomba")
    if e2=="mamifero":
        if e3=="onivoro":
            print("homem")
        elif e3=="herbivoro":
            print("vaca")

def invertebrado(e2,e3):
    if e2=="inseto":
        if e3=="hematofago":
            print("pulga")
        elif e3=="herbivoro":
            print("lagarta")
    if e2=="anelideo":
        if e3=="onivoro":
            print("minhoca")
        elif e3=="hematofago":
            print("sanguessuga")
if __name__ == "__main__":
    e1="invertebrado"
    e2="anelideo"
    e3="hematofago"
    if e1=="vertebrado":
        vertebrado(e2,e3)
    elif e1=="invertebrado":
        invertebrado(e2,e3)
