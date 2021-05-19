def Case_1(R, G, B):
    P = (0.3*R+0.59*G+0.11*B)
    print("Case 1:\n eye= %d" % (P))


def Case_2(R, G, B):
    P = (R+G+B)/3
    print("Case 2:\n Mean= %d" % (P))


def Case_3(R, G, B):
    RGB = [R, G, B]
    for i in RGB:
        if i == max(RGB):
            print("Case 3:\n Max= %d" % ((max(RGB))))
        else:
            print("Case 3:\n Min= %d" % ((min(RGB))))


# main
if __name__ == "__main__":
    # restringir o valor do input de T
    # laço de rept. 1 T 100
    # caso 3 imprimir o max ou o min

    N_case = 50
    R = 23
    G = 78
    B = 197
