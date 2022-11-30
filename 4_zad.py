def The_List():
    list = []
    for i in range(num):
        list.append(input("Enter a list element: "))
    return list
        
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
 
 
num = int(input("Enter a number of elements to add in the list: "))
the_list = The_List()
print(f"\nThe list is: {the_list} ")
 
list_alpha = []
list_num = []
list_other = []
 
for x in the_list:
    if x.isalpha():
        list_alpha.append(x)
    elif x.isnumeric() or isfloat(x):
        list_num.append(float(x))
    else:
        list_other.append(x)
 
 
print(f"\nSplitting The list in three:") 
print(f"In text: {list_alpha}")
print(f"In numbers: {list_num}")
print(f"In others: {list_other}")
 
sum_list_num = sum(list_num)
print(f"\nThe sum of the number list is: {sum_list_num}")
 
start = 0
end = len(list_num)
step = 2
count_list = 0
print(f"\nSplitting the number list into equal parts:")
for i in range(start, end, step):
    x = i
    count_list += 1
    if count_list > 1:
        print("-----------------------------------------------------")
    
    print(f"Split list #{count_list} is: {list_num[x : x+step]}")
    print(f"The max value from the split list #{count_list} is: {max(list_num[x : x+step])}")