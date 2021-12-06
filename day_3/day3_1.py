f = open("day_3/input_data_1.txt", "r")
binary_inputs = f.readlines()
from collections import defaultdict

col_value_count = defaultdict(int)
for binary in binary_inputs:
    for idx, val in enumerate(binary):
        if val.strip() != '':
            col_value_count[(idx, int(val.strip()))] += 1

gamma_rate_string = ""
epsilon_rate_string = ""
for i in range(len(binary_inputs[0])-1):
    if col_value_count[(i, 0)] > col_value_count[(i, 1)]:
        gamma_rate_string += "0"
        epsilon_rate_string += "1"
    else:
        epsilon_rate_string += "0"
        gamma_rate_string += "1"

gamma_rate = int(gamma_rate_string, 2)
epsilon_rate = int(epsilon_rate_string, 2)

print("The gamma_rate times the epsilon rate is: {}".format(gamma_rate * epsilon_rate))