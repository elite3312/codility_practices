

def solution(B):
    taken=dict()
    N=len(B)
    M=len(B[0])
    res=[0,0,0]
    for r in range(N):
        for c in range(M): 
            taken[r,c]=False
    for r in range(N):
        for c in range(M): 
            if B[r][c]=="#"and not taken[r,c]:
                taken[r,c]=True
                if (c-2)>=0 and not taken[r,(c-1)]and B[r][c-1]=="#"   and not taken[r,(c-2)]and B[r][c-2]=="#":
                    res[2]+=1
                    taken[r,c-1]=True
                    taken[r,c-2]=True
                elif (r-2)>=0 and not taken[(r-2),c] and B[r-2][c]=="#"  and not  taken[(r-1),c]and B[r-1][c]=="#":
                    res[2]+=1
                    taken[r-2,c]=True
                    taken[r-1,c]=True
                elif c+2<=(M-1) and not taken[r,c+1] and B[r][c+1]=="#" and not taken[r,c+2]and B[r][c+2]=="#":
                    res[2]+=1
                    taken[r,c+1]=True
                    taken[r,c+2]=True
                elif r+2<=(N-1) and not taken[r+1,c]and B[r+1][c]=="#"  and not  taken[r+2,c]and B[r+2][c]=="#":
                    res[2]+=1
                    taken[r+1,c]=True
                    taken[r+2,c]=True

                elif (c-1)>=0 and not taken[r,(c-1)] and B[r][c-1]=="#"and (r-1)>=0 and not taken[(r-1),c]and B[r-1][c]=="#":
                    res[2]+=1
                    taken[r,c-1]=True
                    taken[r-1,c]=True
                elif (r-1)>=0 and not taken[(r-1),c] and B[r-1][c]=="#" and c+1<=(M-1) and not taken[r,c+1] and B[r][c+1]=="#":
                    res[2]+=1
                    taken[r-1,c]=True
                    taken[r,c+1]=True
                elif c+1<=(M-1) and not taken[r,c+1] and B[r][c+1]=="#"and r+1<=(N-1) and not taken[r+1,c]and B[r+1][c]=="#":
                    res[2]+=1
                    taken[r,c+1]=True
                    taken[r+1,c]=True
                elif r+1<=(N-1) and not taken[r+1,c] and B[r+1][c]=="#" and (c-1)>=0 and not taken[r,(c-1)]and B[r][c-1]=="#":
                    res[2]+=1
                    taken[r+1,c]=True
                    taken[r,c-1]=True

                elif (c-1)>=0 and not taken[r,(c-1)]and B[r][c-1]=="#":
                    res[1]+=1
                    taken[r,c-1]=True
                elif (r-1)>=0 and not taken[(r-1),c]and B[r-1][c]=="#":
                    res[1]+=1
                    taken[r-1,c]=True
                elif c+1<=(M-1) and not taken[r,c+1]and B[r][c+1]=="#":
                    res[1]+=1
                    taken[r,c+1]=True
                elif r+1<=(N-1) and not taken[r+1,c]and B[r+1][c]=="#":
                    res[1]+=1
                    taken[r+1,c]=True

                else:
                    res[0]+=1

    return res
  
if __name__ == "__main__":
    
    s=[".##.#",
       "#.#..",
       "#...#",
       "#.##."]#212
    ans=solution(s)
    print(ans)