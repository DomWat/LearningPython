names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]
new_list = []

for i in names:
    if i not in new_list:
        new_list.append(i)

print(new_list)