
l=[1,2,3,4,5]
k=int(input())
rotation = k % len(l)
print(l[-rotation:]+l[:-rotation])
