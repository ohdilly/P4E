# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    lar = line.split(":")
    tot = tot + float(lar[1])

print("Average spam confidence: ", tot/count)

