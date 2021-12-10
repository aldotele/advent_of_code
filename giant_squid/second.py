f = open('puzzle.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

extracted_numbers = lines[0].split(',')

combo = "XXXXX"  # winning combo used in checks
grids = []
grid = []
winning_picture = {}  # takes picture of the grid when it won
grid_wins_with_number = {}  # associates the number that made a grid win

for el in lines[1:]:
    if el == "" and len(grid) > 0:
        grids.append(grid)
        grid = []
    if not el == "": 
        grid.append(el.split())
grids.append(grid)  # make sure of appending the last at end of file


def mark_grids(game_grids, n):
    marked_grids = []

    for g in game_grids:
        current_grid = []
        for row in g:
            row = ["X" if x == n else x for x in row]
            current_grid.append(row)
        marked_grids.append(current_grid)
    return marked_grids


def check_grids(grids, winning_grids, last_extracted_number):
    new_winning_grids = []
    grid_number = 0
    for g in grids:
        grid_number += 1

        # ROW CHECK
        if "".join(g[0]) == combo or "".join(g[1]) == combo or "".join(g[2]) == combo or "".join(g[3]) == combo or "".join(g[4]) == combo:
            if grid_number not in winning_grids and grid_number not in new_winning_grids:
                new_winning_grids.append(grid_number)
                winning_picture[str(grid_number)] = g
                grid_wins_with_number[str(grid_number)] = last_extracted_number

        # COLUMN CHECK
        if ((g[0][0] + g[1][0] + g[2][0] + g[3][0] + g[4][0]) == combo) or ((g[0][1] + g[1][1] + g[2][1] + g[3][1] + g[4][1]) == combo) or ((g[0][2] + g[1][2] + g[2][2] + g[3][2] + g[4][2]) == combo) or ((g[0][3] + g[1][3] + g[2][3] + g[3][3] + g[4][3]) == combo) or ((g[0][4] + g[1][4] + g[2][4] + g[3][4] + g[4][4]) == combo):
            if grid_number not in winning_grids and grid_number not in new_winning_grids:
                new_winning_grids.append(grid_number)
                winning_picture[str(grid_number)] = g
                grid_wins_with_number[str(grid_number)] = last_extracted_number

    if len(new_winning_grids) > 0:
        for g in new_winning_grids:
            winning_grids.append(g)
        return True, winning_grids

    return False


def compute_score(winning_grid, last_n):
    # winning score is the sum of unmarked numbers on the last winning grid multiplied by the last extracted number
    sum_of_unmarked = 0
    for row in winning_grid:
        for el in row:
            if el != "X":
                sum_of_unmarked += int(el)
    return sum_of_unmarked * last_n


if __name__ == "__main__":
    game_grids = grids.copy()
    n_grids = len(game_grids)
    winning_grids = []
    winning_grid_with_number = {}

    for n in extracted_numbers:
        game_grids = mark_grids(game_grids, n)
        check = check_grids(game_grids, winning_grids, n)

    last_winning_grid = winning_picture[str(winning_grids[-1])]
    winning_n_of_last_winning_g = int(grid_wins_with_number[str(winning_grids[-1])])
    score = compute_score(last_winning_grid, winning_n_of_last_winning_g)
    print("Winning Score is", score)