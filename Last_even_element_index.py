n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if(a[i]%2==0):
        print(i)
        break