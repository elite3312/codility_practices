'''A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].'''
 




from tkinter.tix import MAX


def solution1(A:list):#incorrect
    n=len(A)
    B=sorted(A)
    print(B)
    max=-1000000000
    for i in range(n-2):
        
        index=-i-1
        
        res=B[index-2]*B[index-1]*B[index]
        if(res>max):max=res

    return max
def solution(A:list):
    B=sorted(A)
    print(B)
    product_of_2=0
    if B[0]<0 and B[1]<0:
        product_of_2=B[0]*B[1]
    
    return max(product_of_2*B[-1],B[-1]*B[-2]*B[-3])
    

if __name__ == "__main__":
    A=[4,2,2,5,1,5,8]
    print(solution(A))
    A= [-5, 5, -5, 4]
    print(solution(A))
    A=[-3,1,2,-2,5,6]
    print(solution(A))