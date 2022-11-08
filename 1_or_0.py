num = int(input('num ='))
binary_num = format(num, 'b')
print(binary_num)

my_list = []
for x in str(binary_num):
    my_list.append(int(x))
print(my_list)    

print(my_list[-5])