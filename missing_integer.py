


def solution(A:list)->int:

    A.sort()
    start=False
    d=dict()
    for i in range(len(A)):
        if(not start and A[i]>0):start=True
        if(start):
            if(A[i] not in d.keys()):d[A[i]]=0
            else :d[A[i]]+=1
    ans=1
    for elem in d:#keys are not sorted
        if(ans==elem):ans+=1
        else:
            return ans
    
    return ans
        




if __name__ == "__main__":
  A=[1,3,6,4,1,2]
  
  print(solution(A))
  

  
 