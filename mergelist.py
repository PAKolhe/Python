# Read the first list from the user
list1 = input("Enter the elements of the first list separated by space: ").split()
list1 = [int(x) for x in list1]
# Read the second list from the user
list2 = input("Enter the elements of the second list separated by space: ").split()
list2 = [int(x) for x in list2]
#merge both list
list3= list1+list2
print("Merged List: ", list3)
print("List in Ascending Order: ", sorted(list3))