
vizh=input()
vizh=vizh.split()
pop=vizh[0]
y=vizh[1]
count=0
o=0
while(o<len(pop) and count<2):
    if(pop[o]!=y[o]):
        count+=1
    o+=1
if(count==1 or count==0):
    print("yes")
else:
    print("no")
