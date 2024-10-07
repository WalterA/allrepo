arr = [37,12,28,9,100,56,80,5,12]
index=0
gruppo = arr[1:3]
k=3
print(gruppo)
for i in range(0 , len(arr), k):
    k+=i
    print(arr[i:k])
    