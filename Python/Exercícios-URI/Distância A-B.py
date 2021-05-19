import math

def distance(x1,x2,y1,y2):
    A=pow((x2-x1),2)
    B=pow((y2-y1),2)
    distance=math.sqrt(A+B)
    return distance
#main
if __name__ == "__main__":
    x1=-2.5
    y1=0.4
    x2=12.1
    y2=7.3
    if x1==0 and x2==0 and y1==0 and y2==0:
        print("ponto na origem: (x,y) = (0,0)")
        
print("distância: ", round(distance(x1,x2,y1,y2),3))