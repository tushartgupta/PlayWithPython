def computepay(h,r):
    if h <= 40:
        pay = h * r
        return pay
    else:
        pay = (10.50 * 40) + ((h - 40) * 1.5 * 10.5)
        return pay

hrs = raw_input("Enter Hours:")
hours = float(hrs)
rt = raw_input("Enter Rate:")
rate = float(rt)
p = computepay(hours,rate)
print "Pay",p