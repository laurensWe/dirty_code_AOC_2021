f = open("day_5/input_data_1.txt", "r")
hydro_vent_lines = f.readlines()
from collections import defaultdict
ocean_floor = defaultdict(int)

for vent_line in hydro_vent_lines:
    start_pos, end_pos = vent_line.split(' -> ')
    x1, y1 = [int(x) for x in start_pos.split(',')]
    x2, y2 = [int(x) for x in end_pos.split(',')]
    if x1 == x2:
        # vertical line
        if y1 > y2:
            down_to_up = False
            y2 -= 1
        else:
            down_to_up = True
            y2 += 1

        curr_y = y1
        while curr_y != y2:
            ocean_floor[(x1, curr_y)] += 1
            if down_to_up:
                curr_y += 1
            else:
                curr_y -= 1
    elif y1 == y2:
        # horizontal line
        if x1 > x2:
            left_to_right = False
            x2 -= 1
        else:
            left_to_right = True
            x2 += 1

        curr_x = x1
        while curr_x != x2:
            ocean_floor[(curr_x, y1)] += 1
            if left_to_right:
                curr_x += 1
            else:
                curr_x -= 1
    else:
        # diagonal lines
        if x1 > x2:
            if y1 > y2:
                # linksboven naar rechtsonder +1 +1
                curr_x = x1
                curr_y = y1
                x2 -= 1
                while curr_x != x2:
                    ocean_floor[(curr_x, curr_y)] += 1
                    curr_x -= 1
                    curr_y -= 1
            else:
                # linksonder naar rechtsboven +1 -1
                curr_x = x1
                curr_y = y1
                x2 -= 1
                while curr_x != x2:
                    ocean_floor[(curr_x, curr_y)] += 1
                    curr_x -= 1
                    curr_y += 1
        else: 
            if  y1 > y2:
                # rechtsboven naar linksonder -1 +1
                curr_x = x1
                curr_y = y1
                x2 += 1
                while curr_x != x2:
                    ocean_floor[(curr_x, curr_y)] += 1
                    curr_x += 1
                    curr_y -= 1
            else:
                # rechteronder naar linksboven -1 -1 
                curr_x = x1
                curr_y = y1
                x2 += 1
                while curr_x != x2:
                    ocean_floor[(curr_x, curr_y)] += 1
                    curr_x += 1
                    curr_y += 1

crossing_count = 0
for key, val in ocean_floor.items():
    if val > 1:
        crossing_count += 1

print(crossing_count)