arr = input("enter").split()
arr = [ int(num) for num in arr ]

for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    
    while( j >= 0 and  key < arr[i]):
        arr[j +1] =arr[j]
        j -= 1
    
    arr[j +1] = key
    
print(arr)
    
    




