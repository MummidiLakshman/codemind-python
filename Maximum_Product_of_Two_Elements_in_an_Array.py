a=list(map(int,input().split()))
s=max(a)
a[a.index(s)]=min(a)
h=max(a)
d=(s-1)*(h-1)
print(d)