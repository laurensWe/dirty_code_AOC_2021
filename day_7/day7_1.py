f = open("day_7/input_data_1.txt", "r")
from statistics import median
hor_pos_crabs = f.readlines()[0]
from collections import defaultdict

hor_pos_crabs = [int(x) for x in hor_pos_crabs.split(',')]
median_pos = median(hor_pos_crabs)

total_fuel = 0
for crab in hor_pos_crabs:
    total_fuel += abs(median_pos - crab)

print(total_fuel)

