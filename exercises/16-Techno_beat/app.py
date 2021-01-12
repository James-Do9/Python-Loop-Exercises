



def lyrics_generator(input_array):
    string = ""
    count = 0
    for num in range(0, len(input_array)):
        if input_array[num] == 0:
            string = string + "Boom "
        elif input_array[num] == 1:
            string = string + "Drop the base "
            count = count + 1
            if count == 3:
                string = string + "!!!Break the base!!!"
    return string


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))