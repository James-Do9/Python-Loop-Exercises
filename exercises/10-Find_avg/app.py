my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
num = 0
for i in range(0, len(my_list)):
    num = my_list[i] + num
average = num / len(my_list)
print(average)