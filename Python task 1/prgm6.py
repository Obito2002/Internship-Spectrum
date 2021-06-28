#Q.no-> 6 
#Finding the number of reps of string 'f' in a given string 's'.
def no_of_reps(txt, pat):
    n=len(txt)
    m=len(pat)
    lps=[0]*m
    define_lsp(pat,m , lps)
    i=0
    j=0
    count=0
    while i<n:
        if pat[j]==txt[i]:
            j+=1
            i+=1
        else:
            if j!=0:
                j=lps[j-1]
                
            else:
                j+=1
                i+=1
        if j==m:
            count+=1
            j=lps[j-1]
            
    print(count)


def define_lsp(pat , m ,lps):
    j=0
    i=1
    while i<m:
        if pat[i]==pat[j]:
            lps[i]=j+1
            j+=1
            i+=1
        else:
            if j!=0:
                j=lps[j-1]
            
            else:
                lps[i]=0
                i+=1
    

            
val=input("Enter the string : ")
rpat=input("Enter the pattern :")
no_of_reps(val, rpat)
