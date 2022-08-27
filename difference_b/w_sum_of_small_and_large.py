n=input()
n=n.split()
f=0
d=0
for i in n:
    s=(ord(max(i)))
    p=(ord(min(i)))
    f+=s
    d+=p
    g=abs(f-d)
print(g)
    