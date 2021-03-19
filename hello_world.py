fhand = open('romeo.txt')
alphabet = "abcdefghijklmnoprstuvwxyz"
d = dict()
for sent in fhand:
    sent = sent.rstrip().lower()
    for char in sent:
        if char in alphabet:
            d[char] = d.get(char, 0) + 1

l = list()
for key, value in d.items():
    l.append((value, key))

l.sort(reverse=True)

for v,k in l:
    print(k, v)
