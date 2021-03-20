import re
hand = open('mbox.txt')
count = 0
sum = 0


for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    if len(x) > 0:
        count += 1
        sum += int(x[0])

print(int(sum / count))
