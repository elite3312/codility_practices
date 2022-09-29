

def solution(B):
    taken=dict()
    N=len(B)#r
    M=len(B[0])#c
    res=[0,0,0]
    for r in range(N):
        for c in range(M): 
            taken[r,c]=False
    
    def inner(r:int,c:int,depth:int):

        if (depth>2):return 0
        if (r<0 or r>=N or c<0 or c>=M):return 0
        if (B[r][c]!='#' or taken[r,c]):return 0
        #visit
        taken[r,c]=True
        #visit children
        left=inner(r,c-1,depth+1)
        up=inner(r-1,c,depth+1)
        right=inner(r,c+1,depth+1)
        down=inner(r+1,c,depth+1)
         
        stuff_from_child=left+up+right+down
        
        
        return stuff_from_child+1
    for r in range(N):
        for c in range(M): 
            ret=inner(r,c,0)
            if ret>0:
                if ret==1:
                    res[0]+=1
                elif ret==2:
                    res[1]+=1
                elif ret==3:
                    res[2]+=1
    return res
  
if __name__ == "__main__":
    # # for ship, . for empty
    '''
    s=[".##.#",
       "#.#..",
       "#...#",
       "#.##."]#212
    '''
    s=[".#..#","##..#","...#."]#111
    ans=solution(s)
    print(ans)