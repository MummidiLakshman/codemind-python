import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
d=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(d)
print(format(area,'.2f'))