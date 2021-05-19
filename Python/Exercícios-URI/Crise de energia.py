''' 1031 '''
def criar_regioes(N,regioes):
    for i in range (1,(N+1),1):
        regioes.append(i)

def shut_down(regioes,m):
    i=0
    while i<=(len (regioes)-1):
        regioes[i]=0
        i=i+m
    i=0
    while i<=(len (regioes)-1):
        if regioes[i]==0:
            del (regioes[i])
        else:
            i+=1

def failure(regioes):
    for r in regioes:
        if r==13:
            print ("pos 13: ", regioes.index (r))
            return True
    return False
    
if __name__ == "__main__":
    N = 13
    m=1
    while m<=20:
        print("valor do m: ", m)
        regioes=[]
        criar_regioes(N,regioes)
        #print (regioes)
        shut_down(regioes,m)
        while failure(regioes):
            shut_down(regioes,m)
            print ("resultado Shut: ", regioes)
        m+=1