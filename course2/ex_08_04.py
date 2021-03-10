#exersise 8.4 for the week 4 python data structures course
fname = input("Enter file name: ")
fh = open(fname,'r')
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word in lst: continue
        else:
            lst.append(word.strip())
lst.sort()
print(lst)
