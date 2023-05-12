def solution_wrong(A:list):
    n=len(A)
    sum1=0
    sum2=0
    for i in range(1,n+1):# the sum of a seq from 1 to n
        sum1+=i
    for i in range(n):
        sum2+=A[i]
 
    return abs(sum1-sum2)
def solution(A:list):
    n=len(A)
    
    dict_a=[False for _ in range(0,n+1)]
    
    requires_move=[]
    for e in A:
        if e >n:
            requires_move.append(e)
            continue
        if dict_a[e]==False:
            dict_a[e]=True
        else:
            requires_move.append(e)
    target=[]
    for i in range(1,n+1):
        if dict_a[i]==False:target.append(i)


    requires_move.sort()
    target.sort()

    res=0
    for i in range(len(target)):
        res+=abs(target[i]-requires_move[i])
        if res>=1000000000:return -1
    return res

            


if __name__ == "__main__":
    

    A=[2,1,2]
    ans=solution(A)
    expect=1
    print(A,ans,expect)

    A=[5,1,1,1,1,5]
    ans=solution(A)
    expect=7
    print(A,ans,expect)

    A=[2,2,2,2]
    ans=solution(A)
    expect=4
    print(A,ans,expect)


    A=[2,1,4,4]
    expect=1
    ans=solution(A)
    print(A,ans,expect)

    A=[6,2,3,5,6,3]
    expect=4
    ans=solution(A)
    print(A,ans,expect)
    