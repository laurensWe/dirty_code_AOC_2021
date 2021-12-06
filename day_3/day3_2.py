f = open("day_3/input_data_1.txt", "r")
binary_inputs = f.readlines()
from collections import defaultdict

col_value_count = defaultdict(int)
# find O2
count_0 = 0
count_1 = 0
binary_start = ""
subset_binary = []
for i in range(len(binary_inputs[0])-1):
    for binary in binary_inputs:
        if binary_start == "10111":
            print(binary)
        if binary.startswith(binary_start) or binary == binary_start:
            if binary_start == "10111":
                print("in loop")
                print(binary)
            if binary[i] == "1":
                count_1 += 1
            else:
                count_0 += 1
    
    if len(subset_binary) == 1:
        break
    if count_1 >= count_0:
        binary_start += "1"
    else:
        binary_start += "0"
    subset_binary = []
    count_0 = 0
    count_1 = 0


o2_scrubber = 0
if len(binary_start) == len(binary_inputs[0])-1:
    o2_scrubber = int(binary_start, 2)
else: 
    o2_scrubber = int(subset_binary[0], 2)

# find cO2
count_0 = 0
count_1 = 0
binary_start = ""
subset_binary = []
for i in range(len(binary_inputs[0])-1):
    # print("NEW" + str(binary_start))
    for binary in binary_inputs:
        if binary.startswith(binary_start):
            subset_binary.append(binary)
            # print(binary)
            # print(binary[i])
            if binary[i] == "1":
                count_1 += 1
            else:
                count_0 += 1
    if len(subset_binary) == 1:
        break
    if count_1 < count_0:
        binary_start += "1"
    else:
        binary_start += "0"
    subset_binary = []
    count_0 = 0
    count_1 = 0

co2_scrubber = 0
if len(binary_start) == len(binary_inputs[0])-1:
    co2_scrubber = int(binary_start, 2)
else: 
    co2_scrubber = int(subset_binary[0], 2)

print(o2_scrubber)
print(co2_scrubber)

print("The oxygen times the carbondioxide is: {}".format(o2_scrubber * co2_scrubber))