A=[3,4,4,6,1,4,4]
N=5

def maxCounters(N, A):
    counters = [0] * N
    # loop que verifica se o valor e menor que o tamanho do array
    for value in A:
        if value <= N:
            counters[value-1] += 1
        else:
            # recebe o maximo contador * o tamanho do array
            counters = [max(counters)] * N
    return counters

# main
if __name__ == "__main__":
    print(A)
    print(maxCounters(N,A))    