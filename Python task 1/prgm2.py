#Q.no -> 2
#Program to find the number of zeros in the factorial of the given number:
sum=0

x=int(input("Enter the number :"))
while x<0:
        x=int(input())    

while x>=5:
    sum+=x//5
    x=x//5

print(sum) 