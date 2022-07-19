n=input()
v='aeiouAEIOU'
c=0
p=0
h=0
k=0
for i in n:
    if i in v:
        c+=1
    elif i==' ':
        k+=1
    elif i.isdigit():
        h+=1
    else:
        p+=1
print('Vowels:',c)
print('Consonants:',p)
print('Digits:',h)
print('White spaces:',k)
        
        