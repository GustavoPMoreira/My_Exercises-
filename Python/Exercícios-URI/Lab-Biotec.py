import time
start = time.time()


def simpleCalc(alfabet,values,word):
    sum=0
    for i in range (len(alfabet)):
        for j in word:
            if j== alfabet[i]:
                sum+=values[i]
    print (sum)

if __name__ == "__main__":

    values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
              15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
    alfabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    word = "aacbbc"

    simpleCalc(alfabet,values,word)

    '''test=1
    for i in range (test):
        word=input()'''

done = time.time()
elapsed = done - start
print(elapsed)
