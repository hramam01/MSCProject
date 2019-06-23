import pandas as pd

file = open(r'''/Users/hari/Desktop/CompTestResults.txt''', 'r')

x = [i.strip().split('\t') for i in file.readlines()]
y = list(filter(None, x))
print(y[34915])
print(y[34976])
print(y[34043])