#Q.no -> 3
#Program to find all primes from 1 to n : 
def is_prime(x):
    limit=int(x**0.5)
    i=2
    flag=True
    while(i<=limit and flag == True):
        if x%i==0:
            flag = False
            break
        else:
            i+=1
    return flag

def check_primes(n):
    for i in range(2,n+1):
        flag= is_prime(i)
        if flag:
            print(i, end=" ")

#driver code
value=int(input("Enter the value of n :"))
check_primes(value)


