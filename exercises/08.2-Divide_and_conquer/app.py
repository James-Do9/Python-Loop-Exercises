list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(num_list):
    odd_list = []
    even_list = []
    combined_list = []
    for i in range(0, len(num_list)):
        if num_list[i] % 2 == 0:
            even_list.append(num_list[i])
        else:
            odd_list.append(num_list[i])
    combined_list.append(odd_list)
    combined_list.append(even_list)
    return combined_list


print(merge_two_list(list_of_numbers))

