s = input('Enter Score')
try:
    s=float(s)
    if s >=0.90:
        print("A")
    elif s >=0.80:
        print ("B")
    elif s >=0.70:
        print ("C")
    elif s >=0.60:
        print ("D")
    else:
        print ("print F")
except:
    print ("please enter a score between 0 and 1")
