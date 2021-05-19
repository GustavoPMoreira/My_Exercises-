
# main

if __name__ == "__main__":
    leds=(6,2,5,5,4,5,6,3,7,6)
    Test=1
    r=0
    for i in range (Test):
        n="115380"
        for i in n:
            r=r+leds[int(i)]
        print(r)


#C
'''
int vet[20];
for (i=0;i>20;i++){
    vet[i]=vet[i]+1
}

'''
#Python
#prenceher o vetor no python
'''vet=[]
for i in range (0,20):
    vet.append(i)
print(vet)'''
