
tasks = [
	{ "label": 'Eat my lunch', "done": True },
	{ "label": 'Make the bed', "done": False },
	{ "label": 'Have some fun', "done": False },
	{ "label": 'Finish the replits', "done": False },
	{ "label": 'Replit the finishes', "done": True },
	{ "label": 'Ask for a raise', "done": False },
	{ "label": 'Read a book', "done": True },
	{ "label": 'Make a trip', "done": False }
]


#Your code go here:
def my_function(x):
    for content in x:
        if x["done"] == True:
            return content

new_list = list(filter(my_function, tasks))

print(new_list)



"""done_list = []          one solution
for content in tasks:
    if content["done"] == True:
        done_list.append(content)
print(done_list)"""