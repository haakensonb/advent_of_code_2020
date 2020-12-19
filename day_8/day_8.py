def parse_input(input_file_path):
    instructions = []
    with open(input_file_path) as f:
        for line in f:
            tokens = line.strip().split()
            instruction = tokens[0]
            value = int(tokens[1])
            instructions.append([instruction, value])
    return instructions


def run_code(instructions):
    # Instruction indices that have already been executed.
    executed = set()
    
    is_inf_loop = True
    keep_going = True
    cur_idx = 0
    accumulator = 0
    while keep_going:
        if cur_idx >= len(instructions):
            is_inf_loop = False
            return (is_inf_loop, accumulator)
        # If the instruction has already been ran then we are about to enter
        # an infinite loop as per the problem instructions.
        if cur_idx in executed:
            return (is_inf_loop, accumulator)
        
        executed.add(cur_idx)

        if instructions[cur_idx][0] == 'acc':
            accumulator += instructions[cur_idx][1]
            cur_idx += 1
        elif instructions[cur_idx][0] == 'jmp':
            cur_idx += instructions[cur_idx][1]
        elif instructions[cur_idx][0] == 'nop':
            cur_idx += 1


def flip(instruction):
    if instruction[0] == 'jmp':
        instruction[0] = 'nop'
    elif instruction[0] == 'nop':
        instruction[0] = 'jmp'


def part_2(instructions):
    for instruction in instructions:
        flip(instruction)
        result = run_code(instructions)
        if result[0] == False:
            return result[1]
        # Flip instruction back to orignal value.
        flip(instruction)


if __name__ == "__main__":
    instructions = parse_input("input.txt")
    print("Part 1: ")
    print(run_code(instructions)[1])
    print("Part 2:")
    print(part_2(instructions))