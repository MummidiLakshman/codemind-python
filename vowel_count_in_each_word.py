n=input().lower()
n=n.split()
v='aeiou'
c=0
s=[]
for i in n:
    for j in i:
        if j in v:
            c+=1
    s.append(c)
    c=0
print(*s)
        