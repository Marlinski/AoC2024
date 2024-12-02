import re
import os
file_path = 'day-1/puzzle'

col1 = []
col2 = []

with open(file_path, 'r') as file:
    for line in file:
        parsed = re.split(r'\s+', line.strip())
        col1.append(int(parsed[0]))
        col2.append(int(parsed[1]))

sorted_col1 = sorted(col1)
sorted_col2 = sorted(col2)

res = 0
for i in range(0, len(sorted_col1)):
    a = sorted_col1[i]
    b = sorted_col2[i]
    res += abs(a-b)

print(res)