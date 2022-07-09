a,b=map(int,input().split())
s=list(map(int,input().split()))
c=0
for i in range(0,a):
    t=0
    for j in range(i,a):
        t+=s[j]
        if(t==b):
            c+=1
print(c)
            
            
        