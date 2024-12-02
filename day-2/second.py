import re
file_path = 'day-2/puzzle'

def report_safe(report, dampener=True):
    prev_sign = 0
    
    for i in range(0,len(report)):
        if i == 0:
            continue

        cur_level = report[i]
        prev_level = report[i-1]

        differ = abs(cur_level - prev_level)
        cur_sign = 0 if differ == 0 else (cur_level-prev_level)/differ

        if differ < 1 or differ > 3 or (prev_sign != 0 and prev_sign != cur_sign):
            if not dampener:
                return False
            
            first = report.copy()
            del first[0]
            if report_safe(first, False):
                return True

            left = report.copy()
            del left[i-1]
            if report_safe(left, False):
                return True
            
            right = report.copy()
            del right[i]
            return report_safe(right, False)
        
        prev_sign = cur_sign    
    return True


res = 0
with open(file_path, 'r') as file:
    for line in file:
        parsed = re.split(r'\s+', line.strip())
        if report_safe(list(map(int, parsed))):
            res += 1
print(res)