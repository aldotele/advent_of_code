from collections import Counter


f = open('puzzle.txt', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

# print(lines)

def count_at_index(binary_list, i):
    return Counter([el[i] for el in binary_list])


def extract_most_common(counter):
    if counter["0"] > counter["1"]:
        return "0"
    elif counter["1"] >= counter["0"]:
        return "1"

def extract_least_common(counter):
    if counter["0"] <= counter["1"]:
        return "0"
    elif counter["1"] < counter["0"]:
        return "1"


def compute_ogr(binary_list, n_iter=0):
    current_most_common = extract_most_common(count_at_index(binary_list, n_iter))
    selected = []
    for i in range(len(binary_list)):
        if binary_list[i][n_iter] == current_most_common:
            selected.append(binary_list[i])
    n_iter += 1
    if len(selected) == 1:
        return selected[0]

    return compute_ogr(selected, n_iter)


def compute_csr(binary_list, n_iter=0):
    current_least_common = extract_least_common(count_at_index(binary_list, n_iter))
    selected = []
    for i in range(len(binary_list)):
        if binary_list[i][n_iter] == current_least_common:
            selected.append(binary_list[i])
    n_iter += 1
    if len(selected) == 1:
        return selected[0]

    return compute_csr(selected, n_iter)

ogr = compute_ogr(lines)
csr = compute_csr(lines)

lsr = int(ogr, 2) * int(csr, 2)

print("Life Support Rating is", lsr)
