f = open("day_1/input_data_1.txt", "r")
from collections import defaultdict
depths = f.readlines()

# Make measure_dict 
measure_dict = defaultdict(int)
current_index = 0
measure_dict[0] += int(depths.pop(0).strip())
measure_dict[1] += int(depths.pop(0).strip())
for depth in depths:
    curr_depth = int(depth.strip())
    measure_dict[current_index] += curr_depth
    measure_dict[current_index+1] += curr_depth
    measure_dict[current_index+2] += curr_depth
    current_index += 1

prev_measure = 0
count = -1
for key, value in measure_dict.items():
    if value > prev_measure:
        count += 1
    prev_measure = value

print("Amount of increases for three sliding window: {}".format(str(count)))
