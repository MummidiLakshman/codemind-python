n=input()
n=n.lower()
v='aeiou'
d=[]
c=0
for i in n:
    if i in v:
        c+=1
    else:
        d.append(c)
        c=0
d.append(c)
print(max(d))
        
    
        
        