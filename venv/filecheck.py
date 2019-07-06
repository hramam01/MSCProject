import pandas as pd

file = open(r'''/Users/hari/Desktop/UAT Week 1.txt''', 'r')

x = [i.strip().split('\t') for i in file.readlines()]


flat_list = []
for sublist in x:
    for item in sublist:
        flat_list.append(item)

y = list(filter(None, flat_list))
print(len(flat_list))
print(len(x))
print(len(y))
print(y)
#flatten = lambda l: [item for sublist in l for item in sublist]

#print(flat_list)

