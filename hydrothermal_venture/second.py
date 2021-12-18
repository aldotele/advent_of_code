import numpy as np

f = open('puzzle.txt', 'r')
lines = [line.strip() for line in f]
f.close()

arr = np.zeros((991, 991), dtype=int)


def get_diagonal_points(y1, x1, y2, x2):
    # make y1 <= y2, if you don't need to check, remove this line
    if y1 > y2:
        y1, x1, y2, x2 = y2, x2, y1, x1

    result = []
    slope = (x2 - x1) // (y2 - y1)
    try:
        for i, j in zip(range(y1, y2), range(x1, x2, slope)):
            result.append((i,j))
        result.append((y2,x2))  # add end point
    except ValueError:
        pass
    return result


for el in lines:
    coo = el.split(" -> ")
    coo1 = coo[0].split(',')
    coo2 = coo[1].split(',')
    x1, y1, x2, y2 = int(coo1[0]), int(coo1[1]), int(coo2[0]), int(coo2[1])
    if y1 == y2:
        if x1 <= x2:
            arr[y1, x1:x2+1] += 1
        else:
            arr[y1, x2:x1+1] += 1
    elif x1 == x2:
        if y1 <= y2:
            arr[y1:y2+1, x1] += 1
        else:
            arr[y2:y1+1, x1] += 1
    else:
        points = get_diagonal_points(y1, x1, y2, x2)
        for p in points:
            arr[p[0], p[1]] += 1
     
newArr = arr[arr >= 2]  # filter all elements with at least 2
print("number of points where at least two lines overlap:", len(newArr))



