# Practical 5
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1  

def binary_search(arr, key):
    s, e = 0, len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            s = mid + 1
        else:
            e = mid - 1
    return -1


arr = [1, 2, 3, 4, 5]
key = 3
print("Number",key,"at index:",linear_search(arr,key))
print("Number",key,"at index:",binary_search(arr,key))



  





