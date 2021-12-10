f = open('puzzle.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()
# print(lines)

low_points = []

for i in range(1, len(lines)- 1):
    for j in range(len(lines[i])):
        # considering "middle" points (the ones with 4 adjacent points)
        if 1 <= j <= len(lines[i])-2: 
            if all([
                int(lines[i][j]) < int(lines[i-1][j]),
                int(lines[i][j]) < int(lines[i+1][j]),
                int(lines[i][j]) < int(lines[i][j-1]),
                int(lines[i][j]) < int(lines[i][j+1])
            ]):
                low_points.append(lines[i][j])
        
        # left edges
        if j == 0:
            if all([
                int(lines[i][j]) < int(lines[i-1][j]),
                int(lines[i][j]) < int(lines[i+1][j]),
                int(lines[i][j]) < int(lines[i][j+1]),
            ]):
                low_points.append(lines[i][j])
        
        # right edges
        if j == len(lines[i])-1:
            if all([
                int(lines[i][j]) < int(lines[i-1][j]),
                int(lines[i][j]) < int(lines[i+1][j]),
                int(lines[i][j]) < int(lines[i][j-1]), 
            ]):
                low_points.append(lines[i][j])

# considering top edge
for j in range(1, len(lines[0])-1):
    if all([
        int(lines[0][j]) < int(lines[0][j-1]),
        int(lines[0][j]) < int(lines[0][j+1]),
        int(lines[0][j]) < int(lines[1][j]), 
    ]):
        low_points.append(lines[0][j])


# considering bottom edge
for j in range(1, len(lines[-1])-1):
    if all([
        int(lines[-1][j]) < int(lines[-1][j-1]),
        int(lines[-1][j]) < int(lines[-1][j+1]),
        int(lines[-1][j]) < int(lines[-2][j]), 
    ]):
        low_points.append(lines[-1][j])


# considering the 4 corners
if all([int(lines[0][0]) < int(lines[0][1]), int(lines[0][0]) < int(lines[1][0])]):
    low_points.append(lines[0][0])
if all([int(lines[0][-1]) < int(lines[0][-2]), int(lines[0][-1]) < int(lines[1][-1])]):
    low_points.append(lines[0][-1])
if all([int(lines[-1][0]) < int(lines[-2][0]), int(lines[-1][0]) < int(lines[-1][1])]):
    low_points.append(lines[-1][0])
if all([int(lines[-1][-1]) < int(lines[-1][-2]), int(lines[-1][-1]) < int(lines[-2][-1])]):
    low_points.append(lines[-1][-1])
                 

lp_amount = len(low_points)
lp_sum = 0
for lp in low_points:
    lp_sum += int(lp)

tot_risk_level = lp_sum + lp_amount
print("total risk level is", tot_risk_level)