A=[3, 6, 3, 6, 89]

def oddOccurrencesInArray(A):
    size = len(A)
    b = 0
    for i in range(size):
        b = b ^ A[i]
    return b

if __name__=="__main__":
    print(oddOccurrencesInArray(A))
