f = open('puzzle.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()
# print(lines)


extracted_numbers = lines[0].split(',')
# print(extracted_numbers)

combo = "XXXXX"  # winning combo used in checks
grids = []
grid = []

for el in lines[1:]:
    if el == "" and len(grid) > 0:
        grids.append(grid)
        grid = []
    if not el == "": 
        grid.append(el.split())
grids.append(grid)  # make sure of appending the last at end of file

# print(grids)

def mark_grids(grids, n):
    new_grids = []

    for grid in grids:
        current_grid = []
        for row in grid:
            row = ["X" if x==n else x for x in row]
            current_grid.append(row)
        new_grids.append(current_grid)
    return new_grids


def check_grids(grids):
    grid_number = 0
    for grid in grids:
        grid_number += 1

        # ROW CHECK
        if "".join(grid[0]) == combo or "".join(grid[1]) == combo or "".join(grid[2]) == combo or "".join(grid[3]) == combo or "".join(grid[4]) == combo:
            return True, grid_number, grid

        # COLUMN CHECK
        if (grid[0][0] + grid[1][0] + grid[2][0] + grid[3][0] + grid[4][0] == combo) or (grid[0][1] + grid[1][1] + grid[2][1] + grid[3][1] + grid[4][1] == combo) or (grid[0][2] + grid[1][2] + grid[2][2] + grid[3][2] + grid[4][2]) == combo or (grid[0][3] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] == combo) or (grid[0][4] + grid[1][4] + grid[2][4] + grid[3][4] + grid[4][4] == combo):
            return True, grid_number, grid

    return False, -1


def compute_score(winning_grid, last_number):
    # winning score is the sum of unmarked numbers on the winning grid multiplied by the last extracted number
    sum_of_unmarked = 0
    for row in winning_grid:
        for el in row:
            if el != "X":
                sum_of_unmarked += int(el)
    return sum_of_unmarked * last_number


if __name__ == "__main__":
    game_grids = grids
    for n in extracted_numbers:
        game_grids = mark_grids(game_grids, n)
        check = check_grids(game_grids)
        if check[0] == True:
            last_number = n
            break
    winning_grid = check[2]
    score = compute_score(winning_grid, int(last_number))
    print("Winning Score is", score)