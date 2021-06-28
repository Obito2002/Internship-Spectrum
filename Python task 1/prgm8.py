# Q. no -> 8
#Function to print a pattern starting with x number of stars
def print_stars(x): 
    i=0
    y=x
    while(x>0):
        
        print (" "*i,"* "*x,sep="")
        x-=1
        i+=1
    j=2
    x=y
    while(j<=x):
        print (" "*(y-2),"* "*j,sep="")
        y=y-1
        j+=1

#driver code
print_stars(5)