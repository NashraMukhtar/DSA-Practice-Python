import array as myArray

#Creating an Array
arr1 = myArray.array('i', [1,2,3])
arr2 = myArray.array('u', ['a', 'b', 'c', 'd', 'e'])

#Display using for loop
print("arr1: ")
for i in range(0, len(arr1)):
    print(arr1[i], end=" ")
print("\n")

print("arr2: ")
for i in range(0, len(arr2)):
    print(arr2[i], end=" ")
print("\n")

#Adding value
arr1.insert(0, 0)
arr1.insert(0, -1)
arr1.append(4)

print("after adding values: ")
for i in range(0, len(arr1)):
    print(arr1[i], end=" ")
print("\n")

#Slicing operations
arr3 = arr2[1:3]
print("sliced array: ")
for i in range(0, len(arr3)):
    print(arr3[i], end=" ")
print("\n")

#Negative indexing

