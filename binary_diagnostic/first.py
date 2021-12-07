f = open('puzzle.txt', 'r')
lines = f.readlines()
f.close()

# print(len(lines)) # length of each binary number


gamma = []

for i in range(12):
    n_zeros = 0
    n_ones = 0
    for l in lines:
        if l[i] == "0":
            n_zeros += 1
        elif l[i] == "1":
            n_ones += 1
    if n_zeros > n_ones:
        gamma.append("0")
    else:
        gamma.append("1")

print()
gamma = ''.join(gamma)
print(gamma)

epsilon = ""
for el in gamma:
    if el == '0':
        epsilon += "1"
    elif el == '1':
        epsilon += "0"

print(epsilon)