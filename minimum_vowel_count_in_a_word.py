n=input()
n=n.lower()
v='aeiou'
c=0
s=[]
for i in n.split(" "):
    for j in i:
        if j in v:
            c+=1
    s.append(c)
    c=0
m=min(s)
print(m)

