f = open('puzzle.txt', 'r')
line = f.readline()
f.close()

crubs_positions = [int(el) for el in line.split(",")]
f.close()

max_pos = max(crubs_positions)

tot_fuel = float('inf')  # biggest number of all
pos_to_align = 0

def fuel_to_align(a, b):  # fuel needed to go from a to b
    distance = abs(a - b)
    fuel = 0
    for i in range(1, distance + 1):
        fuel += i
    return fuel

for i in range(max_pos):
    current_tot_fuel = 0
    for el in crubs_positions:
        needed_fuel = fuel_to_align(el, i)
        current_tot_fuel += needed_fuel
    if current_tot_fuel < tot_fuel:
        tot_fuel = current_tot_fuel
        pos_to_align = i


print("position to align is", pos_to_align)
print("needed fuel is", tot_fuel)