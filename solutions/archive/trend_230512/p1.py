def solution(S:str):
    A_count=0#3
    B_count=0#1
    N_count=0#2
    for c in S:
        if c=='A':A_count+=1
        if c=='B':B_count+=1
        if c=='N':N_count+=1
    return int(min(A_count/3,B_count,N_count/2))


if __name__ == "__main__":
    A="XBANANA"
    ans=solution(A)
    expect=1
    print(A,ans,expect)
   
    