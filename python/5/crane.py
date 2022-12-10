import sys
from typing import List

NUM_STACKS = 9

def read_input():
    whole_input = sys.stdin.read().split('\n\n')

    initial_state = whole_input[0]
    instructions = whole_input[1]

    return parse_initial_state(initial_state), parse_instructions(instructions)

def parse_initial_state(block: str) -> List[List[str]]:
    """
    Returns the initial state as a list of lists
    where each sublist corresponds
    to a stack of marked crates.
    """
    state = [[] for x in range(NUM_STACKS)]

    lines = block.splitlines()
    for line in lines[-2::-1]:
        for i, position in enumerate(range(1, len(lines[-1]), 4)):
            block = line[position]
            if line[position] != ' ':
                state[i].append(block)
    return state

def parse_instructions(instruction_block: str):
    """
    Returns the instructions parsed as a list of tuples of integers
    where each tuple of integers is of the form:
    (# of crates to move, initial stack, destination stack)
    """
    instruction_lines = instruction_block.splitlines()

    instructions = [parse_instruction(line) for line in instruction_lines]
    
    return instructions

def parse_instruction(line: str):
    return tuple([int(char) for char in line.split(' ') if char.isnumeric()])

def apply_instruction(state, instruction):
    num_crates = instruction[0]
    initial_stack = instruction[1]
    end_stack = instruction[2]

    for _ in range(num_crates):
        state = operate_crane(state, initial_stack, end_stack)
    
    return state

def operate_crane(state, initial, destination):
    initial -= 1
    destination -= 1

    crate = state[initial].pop()
    print(f"Moving crate {crate} from stack {initial+1} to {destination+1}")

    state[destination].append(crate)

    return state

def show_tops(state):
    for stack in state:
        print(stack.pop(), end='')
    print()

def main():
    state, instructions = read_input()

    for instruction in instructions:
        state = apply_instruction(state, instruction)
    
    show_tops(state)

main()