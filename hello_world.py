enter_file = input("Enter file name: ")
fhand = open(enter_file)
msg_count = {}

for sent in fhand:
    if sent.startswith("Received:"):
        words = sent.split(" ")
        msg_snt = words[2].rstrip()
        msg_count[msg_snt] = msg_count.get(msg_snt, 0) + 1

min = 50
min_email = ""
for key,value in msg_count.items():
    if value < min:
        min = value
        min_email = key

print(min_email, min)

max = 0
max_email = ""

for key,value in msg_count.items():
    if value > max:
        max = value
        max_email = key

print(max_email, max)
