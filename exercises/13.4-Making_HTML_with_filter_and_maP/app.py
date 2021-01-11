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
def generate_li(x):
    for i in x:
        return "<li>" + x[i] + "</li>"

sexy_colors = list(filter(filter_colors, all_colors))
generate_html = list(map(generate_li, sexy_colors))

new_html = ""
for i in range(0, len(generate_html)):
    new_html = new_html + generate_html[i]
print(new_html)
