f = open('test.txt', 'r')
puzzle = [int(el) for el in "".join(f.readline().split(","))]
f.close()
# print(puzzle)


for i in range(80):
    new_puzzle = []
    new_end_of_puzzle = []
    for n in puzzle:
        if n == 0:
            new_puzzle.append(6)
            new_end_of_puzzle.append(8)
        else:
            new_puzzle.append(n - 1)
    puzzle = new_puzzle + new_end_of_puzzle

print(len(puzzle))
    
# alternative using recursion

def lf(puzzle, c):
    if c == 256:
        return len(puzzle)
    new_puzzle = []
    new_end_of_puzzle = []
    for n in puzzle:
        if n == 0:
            new_puzzle.append(6)
            new_end_of_puzzle.append(8)
        else:
            new_puzzle.append(n - 1)
    p = new_puzzle + new_end_of_puzzle
    return lf(p, c+1)  