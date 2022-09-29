# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    res=0
    sums=prefix_sums(A)
    sums=sums[1:]

    uniques=set(A)
    uniques=list(uniques)

    for elem in uniques:
        head=-1
        tail=-1
        for i in range(0,len(A)):
            if A[i]==elem:
                head=i
                break
        if head==-1:continue
        for i in range(len(A)-1,-1,-1):
            if A[i]==elem:
                tail=i
                break
        if tail==-1:continue
        sum=sums[tail]-sums[head]+A[head]
        res=max(res,sum)

    
    return res
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P
  
if __name__ == "__main__":
    s=[1,3,6,1,6,6,9,9]
    #s=[2,2,2,3,2,3]
    ans=solution(s)
    print(ans)