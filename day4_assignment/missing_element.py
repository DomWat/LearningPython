# find a missing element and add it to an array

array = [0, 1, 2, 3, 4, 6, 7, 8, 9]
sec_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in sec_array:
    if i not in array:
        array.append(i)
        print("In this array " + str(i) + " was missing and has now been added.")
array.sort()
print(array)       