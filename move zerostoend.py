l=[1,3,0,4,2,0,9,0]
p=0
for i in range(len(l)):
    if l[i]!=0:
        l[p]=l[i]
        p+=1
print(l)
