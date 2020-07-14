fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
fm = dict()
for ln in fh:
    ln = ln.rstrip()
    if not ln.startswith("From "): continue
    pc = ln.split()
    hr = pc[5].split(':')
    fm[hr[0]]= fm.get(hr[0],0)+1

lst=sorted(fm.items())
for x,y in lst:
    print(x,y)
