fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
fm = dict()
for ln in fh:
    ln = ln.rstrip()
    if not ln.startswith("From "): continue
    pc = ln.split()
    fm[pc[1]]= fm.get(pc[1],0)+1
##print(fm)
cnt = None
Prs = None
for k, v in fm.items():
    if cnt is None or cnt < v :
        Prs = k
        cnt = v

print(Prs, cnt)
