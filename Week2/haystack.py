import re

#hand = open('regex_sum_42.txt')
hand = open('regex_sum_49493.txt')
sum = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for i in x:
            sum += int(i)
print(sum)