puzzle = "4,3,4,5,2,1,1,5,5,3,3,1,5,1,4,2,2,3,1,5,1,4,1,2,3,4,1,4,1,5,2,1,1,3,3,5,1,1,1,1,4,5,1,2,1,2,1,1,1,5,3,3,1,1,1,1,2,4,2,1,2,3,2,5,3,5,3,1,5,4,5,4,4,4,1,1,2,1,3,1,1,4,2,1,2,1,2,5,4,2,4,2,2,4,2,2,5,1,2,1,2,1,4,4,4,3,2,1,2,4,3,5,1,1,3,4,2,3,3,5,3,1,4,1,1,1,1,2,3,2,1,1,5,5,1,5,2,1,4,4,4,3,2,2,1,2,1,5,1,4,4,1,1,4,1,4,2,4,3,1,4,1,4,2,1,5,1,1,1,3,2,4,1,1,4,1,4,3,1,5,3,3,3,4,1,1,3,1,3,4,1,4,5,1,4,1,2,2,1,3,3,5,3,2,5,1,1,5,1,5,1,4,4,3,1,5,5,2,2,4,1,1,2,1,2,1,4,3,5,5,2,3,4,1,4,2,4,4,1,4,1,1,4,2,4,1,2,1,1,1,1,1,1,3,1,3,3,1,1,1,1,3,2,3,5,4,2,4,3,1,5,3,1,1,1,2,1,4,4,5,1,5,1,1,1,2,2,4,1,4,5,2,4,5,2,2,2,5,4,4"
puzzle = "".join(puzzle.split(","))
puzzle = [int(el) for el in puzzle]

for i in range(80):
    new_puzzle = []
    new_end_of_puzzle = []
    for el in puzzle:
        n = int(el)
        if el == 0:
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
    for el in puzzle:
        n = int(el)
        if el == 0:
            new_puzzle.append(6)
            new_end_of_puzzle.append(8)
        else:
            new_puzzle.append(n - 1)
    p = new_puzzle + new_end_of_puzzle
    return lf(p, c+1)  