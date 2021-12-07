f = open('puzzle.txt', 'r')
lines= f.readlines()

c = 0
for i in range(3, len(lines)):
    past_window = int(lines[i-3].strip()) + int(lines[i-2].strip()) + int(lines[i-1].strip())
    current_window = int(lines[i-2].strip()) + int(lines[i-1].strip()) + int(lines[i].strip())
    if current_window > past_window:
        c += 1
f.close()

print(c)
