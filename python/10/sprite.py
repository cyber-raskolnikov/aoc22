import sys

def read_next_instruction():
    return sys.stdin.readline().rstrip()

X_REGISTER = 1
CYCLE = 1
INSTRUCTION = read_next_instruction()

SCREEN = ['.'] * 240

while True:
    if (CYCLE%40) in range(X_REGISTER, X_REGISTER+3):
        SCREEN[CYCLE-1] = '#'

    if INSTRUCTION == "noop":
        # Just pass cycle and read next instruction
        INSTRUCTION = read_next_instruction()
    
    elif INSTRUCTION.startswith("addx"):
        # prepare for second cycle and let this one pass
        INSTRUCTION = "REAL " + INSTRUCTION
    
    elif INSTRUCTION.startswith("REAL addx"):
        # actual execution and let cycle pass
        value = int(INSTRUCTION.split(' ')[2])
        X_REGISTER += value
        INSTRUCTION = read_next_instruction()
    
    elif INSTRUCTION == '':
        break
    
    CYCLE += 1

for i in range(6):
    for j in range(40):
        print(SCREEN[i*40 + j], end=' ')
    print()