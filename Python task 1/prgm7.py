#Q.no -> 7 
#To find a triplet whose sum is a given integer k :
def is_sum(arr,n):
    for i in range(len(arr)):
        add= n -arr[i]
        for i in range(len(arr)-2):
            l=i+1
            h=len(arr)-1
            while(h>l):
                if arr[l]+arr[h]==add :
                    print(arr[i] , arr[l] , arr[h], sep=" ")
                    return 
                
                else:
                    h-=1

            
#driver code 
value=int(input("Enter the number of integers in the array :"))
arr=[0]*value 
for i in range (value):
    arr[i]=int(input())
k=int(input("Enter the value of k :"))
is_sum(arr,k)

