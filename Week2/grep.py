#  Simulating operation of grep command in Unix

import re
hand = open('mbox.txt')
regex = input('Enter a regular expression: ')
count = 0
for line in hand:
    line.rstrip()
    if re.search(regex, line):
        count += 1
print(hand.name, 'had', count, 'lines that matched', regex)
