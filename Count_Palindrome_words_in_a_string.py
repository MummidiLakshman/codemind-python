def rev(a):
    c=0
    s=a[::-1]
    if(s==a):
        return 1
    else:
        return 0
a=input()
a=a.lower()
k=a.split()
c=0
for i in k:
    if(rev(i)):
        c+=1
print(c)
        