a=int(input())
b=int(input())
c=0
def prime(a):
    if(a==1):
        return 0
    for i in range(2,(a//2)+1):
        if(a%i==0):
            return 0
    else:
        return 1
for j in range(a,b+1):
    if(prime(j)):
        print(j)
    

