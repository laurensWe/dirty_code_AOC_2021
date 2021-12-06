f = open("day_6/test_data_1.txt", "r")
hydro_vent_lines = f.readlines()
from collections import defaultdict
ocean_floor = defaultdict(int)

