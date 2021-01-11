people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    new_list = []
    for i in range(0, len(people)):
        if people[i] != person_name:
            new_list.append(people[i])
    return new_list
print(deletePerson('daniella'))
print(deletePerson('juan'))
print(people)