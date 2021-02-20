str="x-dspam-confidence:0.8475"

ipos = str.find(':')
piece = str[ipos+1:]
print (piece)
value = float(piece)
print(value)
