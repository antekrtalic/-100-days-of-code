fhand = open('mbox-short.txt')
d = dict()
count = 0
for sent in fhand:
    check = sent.startswith("From")
    words = sent.split()
    if check and len(words) > 2:
        y = words[5].find(":")
        hour = words[5][:y]
        d[hour] = d.get(hour, 0) + 1


for k,v in d.items():
    print(k,v)

