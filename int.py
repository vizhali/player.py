
vizh,pop=map(int,input().split())
bob=[]
for z in range(vizh,pop+1):
    for p in range(2,z):
        if(z%p==0):
            break
    else:
        bob.append(z)
print(len(bob))
