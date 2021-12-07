f = open('puzzle.txt', 'r')
lines = f.readlines()

horizontal = 0
depth = 0

for l in lines:
    pos, n = l.strip().split()
    n = int(n)
    if pos == "forward":
        horizontal += n
    if pos == "down":
        depth += n
    if pos == "up":
        depth -= n

print("horizontal ", horizontal)
print("depth ", depth)
print(horizontal * depth)