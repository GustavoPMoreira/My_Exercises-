'''corta a string a partir da 3a casa se fosse :2 cortava do final 
(nao necessariamente precisa ser 2), somente para strings'''

N=32
def solution(N):
        binario=str(bin(N))[2:]
        gap=0
        aux_Max=0
        check=False
        for i in binario:
            if i=="1":
                if gap>aux_Max:
                    aux_Max=gap
                check=True
                gap=0        
            elif check:
                 gap+= 1
        return aux_Max

if __name__=="__main__":
    print (binario(N))
    print (solution(N))