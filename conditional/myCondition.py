# hrs = raw_input("Enter Hours:")
# h = float(hrs)
# rate = raw_input("Enter Rate:")
# r = float(rate)
# if h <= 40:
#     pay = h * r
# else:
#     pay = (10.50 * 40) + ((h - 40) * 1.5 * 10.5)
# print pay

score = raw_input("Enter Score: ")
sc = float(score)
if sc < 0:
    print "Value out of range"
    quit()
elif sc > 1.0:
    print "Value out of range"
    quit()
elif sc >= 0.9:
    print 'A'
elif sc >= 0.8:
    print 'B'
elif sc >= 0.7:
    print 'C'
elif sc >= 0.6:
    print 'D'
else:
    print 'F'


