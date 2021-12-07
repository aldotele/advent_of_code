f = open('puzzle.txt', 'r')
lines = f.readlines()

horizontal = 0
depth = 0
aim = 0

for l in lines:
    pos, n = l.strip().split()
    n = int(n)
    if pos == "forward":
        horizontal += n
        depth += aim * n
    if pos == "down":
        aim += n
    if pos == "up":
        aim -= n
f.close()

print("horizontal ", horizontal)
print("depth ", depth)
print(horizontal * depth)