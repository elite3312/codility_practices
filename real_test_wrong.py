
import string

def solution(A:list,B:list,C:list):
    
    letters=list(string.ascii_uppercase)
    digits=list(string.digits)
    
    letters_start=0
    digits_start=0
    for i in range(0,len(C)):
        if(C[i] in digits):
            digits_start=i
        elif(C[i] in letters):
            letters_start=i

    if(digits_start<letters_start):return False

    ############
    
    char=list()
    index_in_A=list()
    index_in_B=list()
    for c in C[0:digits_start]:#letters
        char.append(c)
        index_in_A.append(-1)
        index_in_B.append(-1)
    char_in_A=dict(zip(char,index_in_A))
    char_in_B=dict(zip(char,index_in_B))
    
    for k in char_in_A.keys():
        for i in range(0,len(A)):
            if k==A[i]:
                char_in_A[k]=i

    for k in char_in_B.keys():
        for i in range(0,len(B)):
            if k==B[i]:
                char_in_B[k]=i
    #
    digit=list()
    index_in_A=list()
    index_in_B=list()
    for d in C[digits_start:-1]:#digits
        digit.append(d)
        index_in_A.append(-1)
        index_in_B.append(-1)
    digit_in_A=dict(zip(digit,index_in_A))
    digit_in_B=dict(zip(digit,index_in_B))
    
    for k in digit_in_A.keys():
        for i in range(0,len(A)):
            if k==A[i]:
                digit_in_A[k]=i

    for k in digit_in_B.keys():
        for i in range(0,len(B)):
            if k==B[i]:
                digit_in_B[k]=i
    
    l1=[]
    for i in char_in_A.keys():
        l1.append(char_in_A[i])
    l2=[]
    for i in char_in_B.keys():
        l2.append(char_in_B[i])
    
    l3=[]
    for i in digit_in_A.keys():
        l3.append(digit_in_A[i])
    l4=[]
    for i in digit_in_B.keys():
        l4.append(digit_in_B[i])
        
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print('\n')
    print(sorted(l1))
    print(sorted(l2))
    print(sorted(l3))
    print(sorted(l4))
    
    if sorted(l1) == l1 and sorted(l2) == l2 and sorted(l3) == l3 and sorted(l4) == l4:
        return True
    else:return False
        




if __name__ == "__main__":
  A=['a','b','c','d']
  B=['0','1','c','d']
  C=['a','b','0','1']
  
  print(solution(A,B,C))
  

  
 