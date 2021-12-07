f = open('puzzle.txt', 'r')
lines= f.readlines()

c = 0
for i in range(len(lines)):
    if i == len(lines) - 1:
        break
    if int(lines[i+1].strip()) > int(lines[i].strip()):
        c += 1
f.close()

print(c)

