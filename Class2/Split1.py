fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for ln in fh:
    ln = ln.rstrip()
    if not ln.startswith("From "): continue
    pc = ln.split()
    print(pc[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
