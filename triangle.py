'''An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].'''


def solution(A:list):
    n=len(A)
    if(n<3):return 0
    
    B=sorted(A)
    #print(B)
    index=-1
    for i in range(n):
        if(B[i]>=0):
            index= i
            break
    if index==-1:return 0
    B=B[index:]
    n=len(B)
    #print(B)
    if(n<3):return 0
    
    for i in range(n-2):
        a=B[i]
        b=B[i+1]
        c=B[i+2]
        if( a+b>c and b+c>a and a+c>b ):return 1        
    return 0
if __name__ == "__main__":
    A=[10,50,5,1]#0
    print(solution(A))
    A= [10,2,5,1,8,20]#1
    print(solution(A))
    A=[10, -2147483648, -2147483648]
    print(solution(A))