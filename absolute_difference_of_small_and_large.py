n=input()
n=n.split()
for i in n:
    s=(ord(max(i)))
    p=(ord(min(i)))
    d=abs(s-p)
    print(d,end=' ')
    