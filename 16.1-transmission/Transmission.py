import numpy as np

def process_phase(signal, base_pattern):
    output_list = []
    output_element = 1
    pattern_index = 1
    for _ in signal:
        pattern = get_pattern(base_pattern, output_element)
        output = 0
        working_pattern = pattern.copy()
        while len(working_pattern) < (len(signal) + 1):
            working_pattern.extend(pattern)
        working_pattern = np.asanyarray(working_pattern[1:len(signal) + 1])
        working_signal = np.asanyarray(signal)
        working_product = working_pattern * working_signal
        output = sum(working_product)

        # for value in signal:
        #     output += value * pattern[pattern_index]
        #     pattern_index = (pattern_index + 1) % len(pattern)
        output_list.append(abs(output) % 10)
        pattern_index = 1
        output_element += 1
    return output_list


def get_pattern(pattern, output_element):
    return [val for val in pattern for _ in range(output_element)]


base_pattern = [0, 1, 0, -1]

# input_signal = [int(x) for x in str(12345678)]
# input_signal = [int(x) for x in str(80871224585914546619083218645595)]
input_string = str(
    59704176224151213770484189932636989396016853707543672704688031159981571127975101449262562108536062222616286393177775420275833561490214618092338108958319534766917790598728831388012618201701341130599267905059417956666371111749252733037090364984971914108277005170417001289652084308389839318318592713462923155468396822247189750655575623017333088246364350280299985979331660143758996484413769438651303748536351772868104792161361952505811489060546839032499706132682563962136170941039904873411038529684473891392104152677551989278815089949043159200373061921992851799948057507078358356630228490883482290389217471790233756775862302710944760078623023456856105493) * 10000
input_signal = [int(x) for x in input_string]


print(input_signal)

signal = input_signal
for _ in range(100):
    signal = process_phase(signal, base_pattern)
    print(signal[5970417:8])

print(signal[5970417:8])
