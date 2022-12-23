data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# time -: O(n)
dat = data[0]
print(dat)

# time -: O(n)
for i in data:
    print(i)

# time -: O(n^2)
sum=0
for i in data:
    for j in data:
        sum+=i*j
print(sum)

# time -: O(n*m)
s = 0
for i in range(len(data)):
    for j in range(i):
        s+=(i+j)
print(s)
