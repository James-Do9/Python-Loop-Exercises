theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
new_bools = []
#Your code go here:
def wiki_or_woko(x):
    for i in range(0, len(theBools)):
        if x == 0:
            return ("woko")
        else:
            return ("wiki")
new_list = list(map(wiki_or_woko, theBools))

print(new_list)

