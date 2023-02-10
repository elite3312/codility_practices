'''A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P and Q is an integer within the range [0..N - 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.'''
 



def solution(S:list, P:list, Q:list):
    #A, C, G and T have impact factors of 1, 2, 3 and 4,

    A=[0]
    C=[0]
    G=[0]
    T=[0]
    if S[0]=='A':A[0]=1
    elif S[0]=='C':C[0]=1
    elif S[0]=='G':G[0]=1
    else :T[0]=1

    for i in range(1,len(S)):
        A+=[A[i-1]]
        C+=[C[i-1]]
        G+=[G[i-1]]
        T+=[T[i-1]]
        
        if S[i]=='A':A[i]+=1
        elif S[i]=='C':C[i]+=1
        elif S[i]=='G':G[i]+=1
        else :T[i]+=1
    ans=[]
    A=[0]+A
    C=[0]+C
    G=[0]+G
    T=[0]+T
    for i in range(len(P)):
       
        A_res=A[Q[i]+1]-A[P[i]]
        C_res=C[Q[i]+1]-C[P[i]]
        G_res=G[Q[i]+1]-G[P[i]]
        T_res=T[Q[i]+1]-T[P[i]]
        if A_res!=0:ans+=[1]
        elif C_res!=0:ans+=[2]
        elif G_res!=0:ans+=[3]
        elif T_res!=0:ans+=[4]
        else:
            if S[P[i]]=='A' :ans+=[1]
            elif S[P[i]]=='C':ans+=[2]
            elif S[P[i]]=='G':ans+=[3]
            else :ans+=[4]
    
    return ans

if __name__ == "__main__":
    S='CAGCCTA'  
    P=[2,5,0]
    Q=[4,5,6]
    print(solution(S,P,Q))#2,4,1
    S='AC'  
    P=[0,0,1]
    Q=[0,1,1]
    print(solution(S,P,Q))#1,1,2
    