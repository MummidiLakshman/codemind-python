n=input()
n=n.lower()
c=0
for i in n.split():
    s=i[::-1]
    if(s==i):
        c+=1
print(c)
