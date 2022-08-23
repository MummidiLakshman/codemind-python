n=int(input())
a=list(map(int,input().split()))
g=[]
h=[]
d=0
f=0
for i in range(0,n):
    if(i%2==0):
        g.append(a[i])
    else:
        h.append(a[i])
for i in g:
    d+=i
    #print(d)
for j in h:
    f+=j
    #print(f)
s=abs(d-f)
if(s%4==0):
    print('X')
else:
    print('Y')
#print(a)