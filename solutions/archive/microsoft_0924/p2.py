# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")




def solution(A):
    if len(A)==1:return 0

    tree_sum=sum(A)
    tree_avg=tree_sum//len(A)
    a=sorted(A)
    head=0
    tail=len(a)-1

    res=0
    while head<tail:
        smaller=a[head]
        bigger=a[tail]
        shave_big=bigger-tree_avg
        buff_small=tree_avg-smaller
        action=min(shave_big,buff_small)
        res+=action
        a[tail]=bigger-action
        a[head]=smaller+action
        head+=1
        tail-=1
    curr_max=max(a)
    for elem in a:
        res+=curr_max-elem
    return res

        
    
if __name__ == "__main__":
    #A=[1,2,2,4]
    #A=[4,2,4,6]
    #A=[1,1,2,1]
    A=[1,4]
    res=solution(A)
    print(res)