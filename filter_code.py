import pandas as pd
from pandas import DataFrame, Series
import sys
import os

user_input = raw_input("Enter path of data: ")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
print("Hooray we found your file!")

#stuff you do with the file goes here
file = pd.ExcelFile(user_input)
df = file.parse('Sheet1') 
k = []
for x in df.col1:
	for y in df.col2:
		if x==y: k.append(y)
s = pd.Series(k)
df['col3'] = s
df.to_csv('filter_result.csv')
print 'done'
f.close()
