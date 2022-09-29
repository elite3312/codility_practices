
from cmath import inf


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
    #4 0
    s=bigger//4
    res=s
    #3 1
    s=bigger//3
    if smaller>=s:
        res=max(s,res)
    #2 2
    s=bigger//2
    if smaller>=2*s:
        res=max(s,res)
    #1 3
    s=bigger
    if smaller>=3*s:
        res=max(s,res)
    #0 4
    s=smaller//4
 
    res=max(s,res)
    return res
if __name__ == "__main__":
    #A=10
    #B=21
    A=11
    B=13
    res=solution(A,B)
    print(res)