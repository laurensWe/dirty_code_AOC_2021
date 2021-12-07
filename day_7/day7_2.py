f = open("day_7/input_data_1.txt", "r")
from statistics import mean
from math import floor, ceil
hor_pos_crabs = f.readlines()[0]
from collections import defaultdict

hor_pos_crabs = [int(x) for x in hor_pos_crabs.split(',')]
mean_pos_floor = floor(mean(hor_pos_crabs))
mean_pos_ceil = ceil(mean(hor_pos_crabs))

total_fuel_floor = 0
total_fuel_ceil = 0
for crab in hor_pos_crabs:
    fuel_floor = sum(range(abs(mean_pos_floor - crab)+1))
    fuel_ceil = sum(range(abs(total_fuel_ceil - crab)+1))
    # print("from {0} to {1}, costs {2} fuel".format(crab, mean_pos, fuel))
    total_fuel_floor += fuel_floor
    total_fuel_ceil += fuel_ceil

if total_fuel_ceil > total_fuel_floor:
    print(total_fuel_floor)
else:
    print(total_fuel_ceil)
