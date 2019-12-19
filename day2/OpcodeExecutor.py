import numpy as np

test_input = '1,9,10,3,2,3,11,0,99,30,40,50'


def parse_opcode(opcode):
    ints = list(map(int, opcode.split(',')))
    # with open(input).read().split(',') as ints:
    # for i in opcode.split(','):
    #     operations.append(i)
    return np.array(ints)


def execute_opcode(opcode):

    result = opcode
    result[1] = 12
    result[2] = 2
    i = 0

    def add(i, result):
        result[result[i+3]] = result[result[i+1]] + result[result[i+2]]
        # opcode_flat[line[3]] = opcode_flat[line[1]] + opcode_flat[line[2]]
        # return np.reshape(opcode_flat, (-1, 4))

    def multiply(i, result):
        result[result[i+3]] = result[result[i+1]] * result[result[i+2]]
        # opcode_flat[line[3]] = opcode_flat[line[1]] * opcode_flat[line[2]]
        # return np.reshape(opcode_flat, (-1, 4))

    while result[i] != 99:
        if result[i] == 1:
            add(i, result)
            i = i + 4
        if result[i] == 2:
            multiply(i, result)
            i = i + 4

    return result


input = open('opcode.txt', 'r').read()

print("Before: ", "\n", parse_opcode(input))
print("After: ", "\n", execute_opcode(parse_opcode(input)))

formatted_result = ""
for j in execute_opcode(parse_opcode(input)):
    formatted_result += str(j)
    formatted_result += ','
