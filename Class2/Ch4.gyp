def computepay(h,r):
    if h <= 40:
        return h * r
    else:
        return ((h-40)*(r*1.5)+ (40 * r))

hrs = float(input("Enter Hours: "))
rt = float(input("Enter Rate: "))
p = computepay(hrs,rt)
print("Pay",p)