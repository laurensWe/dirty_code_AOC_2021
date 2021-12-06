f = open("day_2/input_data_1.txt", "r")
commands = f.readlines()

depth = 0
pos = 0
for command in commands:
    dir, val = command.split(' ')
    if dir == "forward":
        pos += int(val.strip())
    if dir == "down":
        depth += int(val.strip())
    if dir == "up":
        depth -= int(val.strip())

print("depth x horizontal position = {}".format(str(depth * pos)))
