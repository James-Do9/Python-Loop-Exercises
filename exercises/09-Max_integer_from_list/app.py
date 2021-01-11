my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]


#Your code go from here:
#my_list.sort() #Easy method by using sort
#print(my_list[-1])

#for i in range(0, len(my_list)): #For loop that uses the max() method
    #if my_list[i] == max(my_list):
        #print(my_list[i])
num = 0
for i in range(0, len(my_list)):
    if my_list[i] > num:
        i = i + 1
        num = my_list[i]
print(num)