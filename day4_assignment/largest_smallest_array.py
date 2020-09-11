# finding the largest element

array1 = [1, 5, 7, 35, 85, 95, 3, 5.5, 12, 0.5]

# option 1 largest and smallest 
array1.sort()
print(array1[-1])
print(array1[0])

# option 2 using a for loop
num = 0


for i in range(0, len(array1)):
    if(array1[i]) > num:
        num = array1[i]
                

print(num)

for i in range(0, len(array1)):
    if(array1[i]) < num:
        num = array1[i]
        
        
print(num)
