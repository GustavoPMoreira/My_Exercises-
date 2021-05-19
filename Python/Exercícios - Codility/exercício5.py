A=[13,15,16,18,17]

def permMissingElem(A):
    size = len(A)
    array_sum = 0
    total = 0
    solver=[]
    n=size+1
   
    for i in range(size):
        if i == min(A):
            continue
        array_sum = array_sum + A[i]
    print(array_sum)
   
    for j in solver and range (n):
            solver[j+min(A)]
    print (solver)
    
    for i in range(min(solver), max(solver), 1):
        if i == min(solver):
            continue
        total = total + i
    print(total)
    return total-array_sum

# main
if __name__ == "__main__":
    print(A)
    print(permMissingElem(A))