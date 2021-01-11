arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sumOdds(array):
    new_array = []
    total = 0
    for i in range(0, len(array)): #This for loop creates a new array with only odd numbers
        if array[i] % 2 != 0:
            new_array.append(array[i])
    for i in range(0, len(new_array)): #This for loop adds all of the odd numbers to each other
        total = total + new_array[i]
    print(total)

sumOdds(arr)
