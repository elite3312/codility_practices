'''Write a function:

class Solution { public int solution(int A, int B, int K); }

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.'''
 
def solution(A:int,B:int,K:int):     
    ans=0
    if(A==0):ans=1
    if(K>A):
        if K>B:
            return ans+0
        if K==B:return ans+1
        else:return ans+1+(B-K)//K
    elif(K==A):
        if K>B:return ans+0
        if K==B:return ans+1
        else:return ans+1+(B-K)//K
    else:
        return ans+1+(B-(A+A%K))//K


def solution2(A:int,B:int,K:int):     
    ans=0
    if(A==0):ans=1
    if(K>A):
        if K>B:
            return ans+0
        if K==B:return ans+1
        else:return ans+1+(B-K)//K
    elif(K==A):
        if K>B:return ans+0
        if K==B:return ans+1
        else:return ans+1+(B-K)//K
    else:
        return ans+1+(B-(A+A%K))//K


def solution1(A:int,B:int,K:int):     
    ans=0
    for i in range(A,B+1):
        if(i % K)==0:
            ans+=1
    return ans

if __name__ == "__main__":
 
  
  print(solution(6,11,2))