s=input()
d=list(s.split())
for i in range(0,len(d)):
    if(i%2==0):
        print(d[i][::-1],end=' ')
    else:
        print(d[i],end=' ')