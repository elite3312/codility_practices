'''You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].'''

def solution1(N:int,A:list):
    #O(n*m)
    counters=[0]*(N+1)
    #print(counters,type(counters))
    max=0
    for elem in A:
        if elem<=N and elem>=1:
            counters[elem]+=1
            if counters[elem]>max:
                max=counters[elem]
        else:
            for i in range(len(counters)):
                counters[i]=max
    return counters[1:]
 
    


def solution0(N:int,A:list):     
    
    counters=[0]*(N+1)
    #print(counters,type(counters))
    _max=0
    bump_to=0
    for i in range(len(A)):
        if 1<=A[i]<=N :
            counters[A[i]]=max(bump_to,counters[A[i]])
            counters[A[i]]+=1
            _max=max(_max,counters[A[i]])
        elif A[i]==(N+1):
            bump_to=_max
    for i in range(1,N+1):
        counters[i]=max(counters[i],bump_to)
    return counters[1:]

if __name__ == "__main__":
  #A=[1,1,4,6,6,6,6,6,1,6]
  #N=5
  #print(solution(N,A))
  #A=[3,4,4,7,1,4,4]
  #N=6
  #print(solution(N,A))
  A=[1,1,1,1,9,1,2,3,4,5,6,7,8,9]
  N=8
  print(solution1(N,A))