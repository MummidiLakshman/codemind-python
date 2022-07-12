a=input()
b=a.split()
for i in b[::-1]:
    g=i
    break
s=min(g)
l=s
if(s.isupper()):
    d=s.lower()
    if d in g:
        print(d)
    else:
        print(l)
else:
    print(s)