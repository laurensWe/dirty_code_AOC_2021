f = open("day_2/input_data_1.txt", "r")
commands = f.readlines()

depth = 0
pos = 0
aim = 0
for command in commands:
    dir, val = command.split(' ')
    val_int = int(val.strip())
    if dir == "forward":
        pos += val_int
        depth += aim * val_int
    if dir == "down":
        aim += val_int
    if dir == "up":
        aim -= val_int

print("depth x horizontal position = {}".format(str(depth * pos)))
