import re

fname = "ActualData_wk2.txt"
fh = open(fname)
tots =0

for ln in fh:
    rd = ln.rstrip()
    nums = re.findall('[0-9]+', rd)
    if len(nums) == 0 :continue
    for num in nums:
        tots = tots + int(num)

print(tots)
