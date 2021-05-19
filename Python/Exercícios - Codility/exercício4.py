x=10
y=85
d=30

def solution(x,y,d):
    return (y-x) // d if (y-x) %d == 0 else (y-x) //d +1
if __name__=="__main__":
    print(solution(x,y,d))