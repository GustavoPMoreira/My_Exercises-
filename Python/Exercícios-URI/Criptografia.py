def Cypher(word):
    code1=list(bytes(word,'utf-8'))#converte a para o valor ASCII encode é utf-8
    for i in range(len(code1)):
        code1[i]+=3#desloca 3 posições
    code2=code1
    code2.reverse()#inverte o vetor
    for i in range((len(code2)//2),len(code2)):#desloca 1 pra esquerda
        code2[i]-=1
    print(code2)
    for i in range(len(code2)):
        code2[i]=chr(code2[i])
    print (code2)

#main
if __name__ == "__main__":
    word="Test#3"
    Cypher(word)