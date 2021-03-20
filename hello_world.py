import re
hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^X-\S*: [0-9.0]+', line):
        print(line)
