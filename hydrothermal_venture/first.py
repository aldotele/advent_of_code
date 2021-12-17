import numpy as np

f = open('puzzle.txt', 'r')
lines = [line.strip() for line in f]
f.close()

arr = np.zeros((991, 991), dtype=int)

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
     
newArr = arr[arr >= 2]  # filter all elements with at least 2

print("number of points where at least two lines overlap:", len(newArr))
