incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:

first_name = []
last_name = []
for content in incomingAJAXData:
    first_name.append(content["name"])
    last_name.append(content["lastName"])
def my_var(x, y):
    return x + " " + y

transformedData = list(map(my_var, first_name, last_name))
print(transformedData)
