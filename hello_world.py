file_name = input("Enter file name: ")
if file_name == "na na boo boo":
    print("NA NA BOO BOO TO YOU TOO - You have been punk'd!")
fhand = open(file_name)
sum = 0
count = 0
total_count = 0
for sent in fhand:
    if sent.startswith("X-DSPAM-Confidence:"):
        x = sent.find(":")
        sum += float(sent[x+1:].strip())
        count += 1

total_count = sum / count
print("Average spam confidence:", total_count)
