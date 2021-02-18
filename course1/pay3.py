def computepay(h,r):
    return h*r

h= input("Enter Hours: ")
r = input ("Enter Rate: ")
try:
    fh = float (h)
    fr = float (r)
except:
    print("Error, please enter numeric input")
    quit()

if fh > 40 :
    reg = fr * fh
    otp = (fh-40) * (fr*.5)
    p= reg + otp
else:
    p = computepay(h,r)
print ("Pay",p)
