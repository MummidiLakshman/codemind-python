n=int(input())
s=n*n
d=0
while(s!=0):
    f=s%10
    d+=f
    s=s//10
if(n==d):
    print("Neon Number")
else:
    print('Not Neon Number')