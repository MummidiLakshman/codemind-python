n=int(input())
a=list(map(int,input().split()))
s=[]
c=0
for i in a:
    if i not in s:
        s.append(i)
for i in s:
    if(i%2==0):
        c+=1
print(c)