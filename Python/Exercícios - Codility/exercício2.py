
A=[3, 8, 9, 7, 6]
K=3
def solution(A,K):
    size=len(A)
    Aux=[0]*size                        #O zero é a posição 1 * size ele se multiplica pelo tamanho do vetor A
    for i in range(size):               #precisa do Mod (%) para evitar i-k = negativo
        Aux[i]=A[(i-K)%size]            #quando é cíclico assim dentre si, precisa-se usar o mod com size
    return Aux

if __name__=="__main__":
    print(solution(A,K))