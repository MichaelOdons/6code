fhand = input('Enter a file name')
fand = open(fhand)
for line in fand:
    line.rstrip()
    print(line)
