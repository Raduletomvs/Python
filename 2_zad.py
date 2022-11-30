
n = int(input("Enter a number for the dict: "))
data = {}
 
for _ in range(n):
    key = input(f"Key: ")
    value = input(f"Value: ")
    data[key] = value
    data.update()
print(f"Dict: {data}")

m = int(input("\nEnter a number for the list: "))
list = []
temp_list = [] 

for i in range(m):
    x = input(f"Enter something for the list: ")
    temp_list.append(x)
    
    if x in data.keys():
        list.append(data.get(x))
        data.pop(x)
    elif x in data.values():
        list.append(data.get(x))
        data.popitem(x)
    elif x not in data.keys():
        list.append(x)
    else: 
        key = input(f"Adding Key for dict:")
        value = input(f"Adding Value for dict:")
        data[key] = value

print(f"List is: {temp_list}\n")
print(f"The new Dict is: {data}")
print(f"The new List is: {list}")