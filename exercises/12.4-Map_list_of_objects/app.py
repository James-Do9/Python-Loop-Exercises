import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]
age_list = []
details_list = []

def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda person:  person["name"] , people))

for content in people:
    age_list.append(content["birthDate"]) #Creates a list with the datetime.datetime 

new_age_list = list(map(calculateAge, age_list)) #Maps through the calculateAge with the age_list array and returns an array with the actual ages

for i in range(0, len(people)):
    details_list.append("Hello, my name is " + str(name_list[i]) + " and I am " + str(new_age_list[i]) + " years old")
print(details_list)

