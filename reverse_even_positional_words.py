s=input()
f=list(s.split())
for i in range(len(f)):
    if(i%2==0):
        print(f[i][::-1],end=' ')
    else:
        print(f[i],end=' ')