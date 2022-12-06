def isfloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
 
n = int(input('Amount of numbers in the list: '))
list = []
list_n = []
 
for _ in range(n):
    list.append(input('Value: '))
print(list)
 
for i in list:
    if i.isnumeric() or isfloat(i):
        list_n.append(float(i))
    else:
        pass
print(list_n)
 
average = sum(list_n) / len(list_n)
print("Average = ", round(average, 2)) 
 
multiplier = int(input("Multiply list by: "))
copy_list_n = list_n.copy()
multiplied_list =[]
 
for bit in copy_list_n:
    rounded_bits = round(bit, 2)
    multiplied_list.append(rounded_bits * multiplier)
print(multiplied_list)
 
multiplied_average = sum(multiplied_list) / len(multiplied_list)
print(f"Average of the list multiplyed by '{multiplier}' =", round(multiplied_average, 2))