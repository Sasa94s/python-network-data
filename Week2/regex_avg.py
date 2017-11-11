#  Write a program to look for lines of the form
#  `New Revision: 39772`
#  and extract the number from each of the lines
#  using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average.

import re
fileName = input('Enter file: ')
hand = open(fileName)
sum = 0
count = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('^N.+: ([0-9.]+)', line)
    if(len(x) > 0):
        for i in x:
            sum += int(i)
            count += 1
print(sum/count)