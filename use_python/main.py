'''A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].'''
 



def solution1(A:list):#o(n**2)
    n=len(A)
    prefix_sum=[0]*n
    prefix_sum[0]=A[0]
    for i in range (1,n):
        prefix_sum[i]=prefix_sum[i-1]+A[i]
    print(prefix_sum)
    min=10000*100000
    min_start_index=-1
    for i in range(n):
        for j in range(i,n):
            sub_len=j-i+1
            sub_sum=0
            avg_sum=0
            if sub_len>1 :
                sub_sum=prefix_sum[j]-prefix_sum[i]+A[i]
                avg_sum=sub_sum/sub_len
            else :continue
            print('(%d,%d)=>%d/%d=%d'%(i,j,sub_sum,sub_len,avg_sum))
            if min>avg_sum:
                min=avg_sum
                min_start_index=i
    return min_start_index
def solution(A:list):
    
    pass
if __name__ == "__main__":
    A=[4,2,2,5,1,5,8]
    print(solution(A))
    #A=[4,-2,2,-5,-1,5,8]
    #print(solution(A))