from queue import LifoQueue

def rnaa_bonds():
    tape="SFBCFSCB"
    count=0
    #construtor
    rnaa=LifoQueue()   
    for e in tape:
        if rnaa.empty():
            rnaa.put(e)
        else:  
            topo=rnaa.get()
            if e =="B" and topo =="S":
                count+=1 
            elif e =="C" and topo=="F":
                count+=1 
            elif e =="F" and topo=="C":
                count+=1
            elif e =="S" and topo=="B":
                count+=1
            else:
                rnaa.put(topo)
                rnaa.put(e)
    print(count)

if __name__ == '__main__':
    rnaa_bonds()

''' else:
    topo=rnaa.get()
    if e=="B" and top=="S" or \
        e=="C" and top=="F" or \
        e=="F" and top=="C" or \
        e=="S" and top=="B":
        count+=1
    else:
        stack.put(top)
        stack.put(e) 
'''