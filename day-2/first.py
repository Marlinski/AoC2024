import re
file_path = 'day-2/puzzle'

def report_safe(report):
    prev_sign = 0
    for i in range(0,len(report)):
        if i == 0:
            continue

        cur_level = int(report[i])
        prev_level = int(report[i-1])

        differ = abs(cur_level - prev_level)
        if differ < 1 or differ > 3:
            return False
        
        cur_sign = (cur_level-prev_level)/differ
        if prev_sign != 0 and prev_sign != cur_sign:
            return False
        
        prev_sign = cur_sign    
    return True

res = 0

with open(file_path, 'r') as file:
    for line in file:
        parsed = re.split(r'\s+', line.strip())
        if report_safe(parsed):
            res += 1

print(res)