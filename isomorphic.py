vizh,pop=map(str,input().split())
if(len(vizh)!=len(pop)):
    print("no")
else :
    f1=[vizh.count(j) for j in vizh]
    f2=[pop.count(j) for j in pop]
if(f1==f2):
    print("yes")
else:
    print("no")
