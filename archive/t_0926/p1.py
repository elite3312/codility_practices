def solution(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1
    occurrences.reverse()#       
    best_char = 'z'#
    best_res = occurrences[0]#

    for i in range(1, 26):
        if occurrences[i] >= best_res:
            best_char = chr(ord('z') - i)#
            best_res = occurrences[i]

    return best_char
    
  
if __name__ == "__main__":
    s="hello"
    #s="cbbaa"
    s="zzzcbbaaa"
    ans=solution(s)
    print(ans)