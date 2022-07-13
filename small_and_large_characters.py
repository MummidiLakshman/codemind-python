n=input()
n=n.lower()
k=n.split(' ')
for i in k:
    s=min(i)
    h=max(i)
    print(s,h,end=' ')