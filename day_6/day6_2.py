f = open("day_6/input_data_1.txt", "r")
import copy
fish_states = f.readlines()
from collections import defaultdict
fish_swarm = defaultdict(int)

if ': ' in fish_states[0]:
    _, init_state = fish_states[0].split(': ')
else:
    init_state = fish_states[0]

for fish_timer in init_state.split(','):
    fish_swarm[int(fish_timer.strip())] += 1

current_day = 0
end_day = 256
new_fish_swarm = defaultdict(int)
while current_day < end_day:
    for fish_time, count in fish_swarm.items():
        if fish_time == 0:
            new_fish_swarm[6] = count
            new_fish_swarm[8] = count
        elif fish_time == 7:
            new_fish_swarm[6] += count 
        else:
            new_fish_swarm[fish_time-1] = count
    fish_swarm = copy.deepcopy(new_fish_swarm)
    # sorting is needed otherwise fish_time 7 will be before 0 :)
    fish_swarm = {key: value for key, value in sorted(fish_swarm.items())}
    print(fish_swarm)
    new_fish_swarm = defaultdict(int)
    current_day += 1

# count the amount of fish in the swarm
total_fish = 0
for fish_time, count in fish_swarm.items():
    total_fish += count

print("total amount of fish in the swarm: {}".format(total_fish))
