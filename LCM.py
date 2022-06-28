a,b=map(int,input().split())
if(a>b):
    x=a
    y=b
else:
    x=b
    y=a
for i in range(1,y+1):
    c=x*i
    if(c%y==0):
        print(c)
        break