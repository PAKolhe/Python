def binary_search(arr, target):

#Function to perform binary search on a sorted list.

 left, right = 0, len(arr) - 1
while left <= right:
 mid = left + (right - left) // 2
# Check if target is present at mid
if arr[mid] == target:
  return mid
# If target is greater, ignore left half
elif arr[mid] < target:
 left = mid + 1
# If target is smaller, ignore right half
else:
 right = mid - 1
# If target is not present in the list
 return -1
input_list = list(map(int,input("Enter the sorted list of numbers separated by space: ").split()))
# Read the target element to search for
target = int(input("Enter the element to search for: "))
# Call binary_search function
result_index = binary_search(input_list, target)
# Print the result
if result_index != -1:
 print(f"Element {target} found at index {result_index}.")
else:
 print(f"Element {target} not found in the list.")
