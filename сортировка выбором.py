a=list(map(int, input().split()))
for i in range(0,len(a)-1):
    amin=a[i]
    for j in range(i+1,len(a)):
        if a[j]<amin:
            amin=j
    a[i],a[amin]=a[amin],a[i]
print(*a)