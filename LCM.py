m,n=map(int,input().split())
if(m>n):
    x=m
    y=n
else:
    x=n
    y=m
for i in range(1,y+1):
    c=x*i
    if(c%y==0):
        print(c)
        break
