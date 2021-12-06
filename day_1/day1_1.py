f = open("day_1/input_data_1.txt", "r")
depths = f.readlines()

count = -1
prev_depth = 0
for depth in depths:
    curr_depth = int(depth.strip())
    if prev_depth < curr_depth:
        count += 1
    prev_depth = curr_depth

print("Amount of increases is: {}".format(str(count)))
