all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

#def generate_li(x):
    #pass
def filter_colors(x):
    for content in x:
        if x["sexy"] == True:
            return x["label"]

sexy_colors = list(filter(filter_colors, all_colors))
print(sexy_colors)
