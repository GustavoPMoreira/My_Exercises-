def caixa_eletronico(N):
    notas=[100,50,20,10,5,2,1]
    for i in notas:
        print("%d nota(s) de R$ %d,00" %(N//i,i))
        N=N%i
if __name__ == "__main__":
    N = 576

    caixa_eletronico(N)
