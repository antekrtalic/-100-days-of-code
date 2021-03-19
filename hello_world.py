fhand = open('mbox-short.txt')
d = dict()
count = 0

for sent in fhand:
    if sent.startswith("From:"):
        words = sent.split()
        email = words[1]
        if email not in d:
            d[email] = 1
        else:
            d[email] += 1

print(d)

l = list()

em_orders = [(v, k) for k,v in d.items()]
em_orders.sort(reverse=True)
print(em_orders)
