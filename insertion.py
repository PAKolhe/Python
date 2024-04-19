""" Implement a Python program to sort an inputted list using insertion sort."""
arr = input("enter list").split()
arr = [int (num) for num in arr]


for i in range (1, len(arr)):
    key = arr[i]
    j = i-1
    
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

print(arr)
