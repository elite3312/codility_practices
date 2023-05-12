


def solution(A, B):
    if A+B<4:return 0
    
    bigger=None
    smaller=None
    if A>=B:
        bigger=A
        smaller=B
    else:
        bigger=B
        smaller=A
    s=(A+B)//4
    while True:
        if bigger>=4*s:return s
        if bigger>=3*s and smaller>=s:return s
        if bigger>=2*s and smaller>=2*s:return s
        #if bigger>=1*s and smaller>=3*s:return s
        #if smaller>=4*s:return s
        s-=1
        if s==0:return 0
        
    
if __name__ == "__main__":
    #A=10
    #B=21
    A=1
    B=8
    res=solution(A,B)
    print(res)