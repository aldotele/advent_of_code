f = open('puzzle.txt', 'r')
lines = [line.strip() for line in f]
f.close()

outputs = []
for l in lines:
    output = l.split(" | ")
    outputs.append(output[1])

counter = 0  # where occurrences of simple digits will be accumulated
considered = [2, 3, 4, 7]  # number of segments in digits 1, 4, 7 and 8
for out in outputs:
    sep = out.split(" ")  # considering digits one by one
    for digit in sep:
        if len(digit) in considered:
            counter += 1

print("digits 1, 4, 7 and 8 together appear", counter, "times")



