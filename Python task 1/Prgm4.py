#Q.no -> 4
#Program to find the gcd of a given array of integers :

def gcd(x,y):

    while(y):
        x, y = y, x % y

    return x

#driver code
value=int(input("Enter the number of integers :"))
arr=[0]*value
for i in range (value):
    arr[i]=int(input())

a=arr[0]
b=arr[1]
rslt=gcd(a,b)

for i in range(2,len(arr)-1):
    rslt=gcd(rslt,arr[i])

print(rslt)



