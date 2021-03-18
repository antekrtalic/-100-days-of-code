fhand = open('mbox-short.txt')
count = 0

for sent in fhand:
    sent.rstrip()
    if sent.startswith("From"):
        sent = sent.split(" ")
        if len(sent) > 2:
            count += 1
            print(sent[1].strip())

print(f"There were {count} lines in the file with From as the first word")
