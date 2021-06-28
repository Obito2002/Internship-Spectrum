#Q.no -> 5
#Program to find the perfect numbers in a given range of integers :
def is_perfect(x):
    sum = 1
    i=2
    while i*i<=x:
        if x%i==0:
            sum+= (i + x//i)
        i+=1


    if sum==x:
        return True
    else:
        return False
    
#driver code
value=int(input("Enter n :"))
x=2
i=0
while (i!=value):
    if is_perfect(x):
        print(x , end=" ")
        i+=1
    x+=1
    

    