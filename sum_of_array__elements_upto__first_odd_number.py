a=int(input())
c=list(map(int,input().split()))
d=0
for i in range(0,a):
    if(c[i]%2!=0):
         break
    else:
        d+=c[i]
print(d)
