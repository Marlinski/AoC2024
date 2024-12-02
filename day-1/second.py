import re

file_path = 'day-1/puzzle'

(col1, col2) = ([], [])
with open(file_path, 'r') as file:
    for line in file:
        parsed = re.split(r'\s+', line.strip())
        col1.append(int(parsed[0]))
        col2.append(int(parsed[1]))

res = 0
for num in col1:
    res += num*col2.count(num)

print(res)