from string import ascii_lowercase

par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for i in ascii_lowercase:
    if par.count(i) != 0:
        counts.update({i : str(par.count(i))})
print(counts)
