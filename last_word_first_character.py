n=input()
s=n.split()
d=''
for i in range(len(s)-1,-1,-1):
    d+=s[i]
    break
for i in range(len(d)):
    print(d[i])
    break
    