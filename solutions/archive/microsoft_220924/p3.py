# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, P, B, E):
    #edge case
    if B==E:return True
    
    #right_boundary
    right_boundary=1000000001
    curr_pos=B
    #determine search direction
    step=1
    displace=E-B
    if displace<0:
        step=-1

    #prepare a dict
    pos_dict=dict()
    for i in range(len(P)):
        pos_dict[P[i]]=A[i]

    while True:
        #setup
        nearest_crane_pos=None
        

        #find nearest crane from the right
        peek_pos=curr_pos
        crane_from_right=None
        while True:
            try:
                if pos_dict[peek_pos]>=1:
                    crane_from_right=peek_pos
                    break
            except :
                peek_pos+=1
                if peek_pos>right_boundary//20:
                    break
        
        
        #find nearest crane from the left
        peek_pos=curr_pos
        crane_from_left=None
        while True:
            try:
                if pos_dict[peek_pos]>=1:
                    crane_from_left=peek_pos
                    break
            except :
                peek_pos+=-1
                if  peek_pos<0:
                    break
        
        if not crane_from_left and not crane_from_right:return False
        elif crane_from_left and not crane_from_right:nearest_crane_pos=crane_from_left
        elif crane_from_right and not crane_from_left:nearest_crane_pos=crane_from_right
        else:
            #diff_left=abs(curr_pos-crane_from_left)
            #diff_right=abs(curr_pos-crane_from_right)

            #nearest_crane_pos=crane_from_left if diff_left<diff_right else crane_from_right

            #if dest is in range of left
            if crane_from_left-pos_dict[crane_from_left]<=E<=crane_from_left+pos_dict[crane_from_left]:
                nearest_crane_pos=crane_from_left
            #if dest is in range of left
            elif crane_from_right-pos_dict[crane_from_right]<=E<=crane_from_right+pos_dict[crane_from_right]:
                nearest_crane_pos=crane_from_right

        #check if nearest crane can reach package
        if nearest_crane_pos-pos_dict[nearest_crane_pos]<=curr_pos and nearest_crane_pos+pos_dict[nearest_crane_pos]>=curr_pos:
            #is within reach

            #check if destination is within reach as well
            if nearest_crane_pos-pos_dict[nearest_crane_pos]<=E and nearest_crane_pos+pos_dict[nearest_crane_pos]>=E:
                #destination is within reach as well
                return True
            else:
                #destination is somewhere else, we can can package at the far end
                if step>0:
                    curr_pos=nearest_crane_pos+pos_dict[nearest_crane_pos]
                else:
                    curr_pos=nearest_crane_pos-pos_dict[nearest_crane_pos]

        else:
            return False
    

        
    
if __name__ == "__main__":
    #ok 1
    #A=[2,1]
    #P=[5,1]
    #B=3
    #E=6
 
    #ok 0 
    #A=[2,1]
    #P=[5,1]
    #B=2
    #E=6

    #ok 1
    A=[1,4,2]
    P=[10,4,7]
    B=11
    E=1

    #ok 1
    #A=[5,5,1]
    #P=[3,3,6]
    #B=4
    #E=8

    #ok 1
    #A=[1,3]
    #P=[2,6]
    #B=1
    #E=5
    res=solution(A,P,B,E)
    print(res)