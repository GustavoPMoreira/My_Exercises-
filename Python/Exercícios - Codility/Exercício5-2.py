A=[13,15,16,18,17]

def permMissingElem(A):

    B = sorted(A)
    number = B[0]

    for i in range(len(B)):
        if B[i]-i != number:            #while(number < A[i]-i):
            for j in range(0, number, 1):
                if number < B[i]-i:
                    missing = i+number
                    number += 1
                return missing   
# main
if __name__ == "__main__":
    print(A)
    print(permMissingElem(A))