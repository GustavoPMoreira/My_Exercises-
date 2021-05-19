import queue

def mining(strg):
    diamonds = queue.LifoQueue()
    count=0
    for e in strg:
        #se achou part.1 add direto
        if e=="<":
            diamonds.put(e)
        #se achou part.2
        elif e==">":
            #verificar se o topo(anterior) é part.1
            #se true pop diamente
            if not diamonds.empty():
                half=diamonds.get()
                if half=="<":
                    count+=1
                else:
                    diamonds.put(half)
                    diamonds.put(e)
            else:
                diamonds.put(e)
        print(diamonds.queue)        
    print(count)

if __name__=="__main__":
    strg=">..<><<><><.....>>><>>>>>....<>>>>>>>>>>><..><.<..>>"
    mining(strg)
    '''strg="<<<..<......<<<<....>"
    mining(strg)
    print (diamonds)'''
