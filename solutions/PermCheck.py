

def solution(A:list):
    n=len(A)
    A.sort()
    for i in range(0,n):
        if(A[i]!=i+1):return 0
    return 1

        




if __name__ == "__main__":
  A=[4,1,3,3]
  
  print(solution(A))
 