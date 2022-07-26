
import string
from tabnanny import check

def solution(A:list,B:list,C:list):
    
    given_digits=list(string.digits)
    given_letters=list(string.ascii_uppercase)
    #print(given_digits)
    #print(given_letters)
    
    letters_start=-1
    digits_start=-1
    for i in range(len(C)):
        if C[i] in given_digits and digits_start==-1:
            digits_start=i
        elif C[i] in given_letters and letters_start==-1:
            letters_start=i
    
    #print(digits_start,letters_start)
    if(digits_start<letters_start):return False

    ############
    letters=C[:digits_start]
    print(letters)
    digits=C[digits_start:]
    print(digits)
    #######
    #check lexographic order
    for i in range(len(letters)):
        if(letters[i] in given_digits):return False
        if not(letters[i]in A or letters[i] in B):return False
    if(sorted(letters)!=letters):return False

    for i in range(len(digits)):
        if(digits[i] in given_letters):return False
        if not(digits[i]in A or digits[i] in B):return False
    if(sorted(digits)!=digits):return False

    return True


        




if __name__ == "__main__":
  A=['A','B','C','D']
  B=['0','1','C','D']
  C=['A','D','0','1']
  
  print(solution(A,B,C))
  
  C=['B','A','0','1']
  print(solution(A,B,C))
 