a= [8,3,1,7,0]

print(a)

for i in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]

print(a)