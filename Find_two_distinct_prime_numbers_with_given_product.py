a=int(input())
def prime(a):
    if(a==1):
        return 0
    for i in range(2,(a//2)+1):
        if(a%i==0):
            return 0
    else:
        return 1
c=0
for i in range(2,(a//2)+1):
    if(prime(i)):
        if(a%i==0):
            c=1
            print(i,end=' ')
if(c==0):
    print('-1')
