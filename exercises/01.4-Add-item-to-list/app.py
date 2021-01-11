#Remember import random function here:
import random 
my_list = [4,5,734,43,45]
def random_num():
    for i in range(10):
        num = random.randint(1, 100)
        my_list.append(num)
random_num()
print(my_list)
#The magic is here:
