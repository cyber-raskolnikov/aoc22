import sys

def read_next_instruction():
    return sys.stdin.readline().rstrip()

X_REGISTER = 1
CYCLE = 1
INSTRUCTION = read_next_instruction()

BREAKPOINTS = [20, 60,100, 140, 180, 220]
SIGNAL_STRENGTHS = []

while True:
    if CYCLE in BREAKPOINTS:
        signal_strength = CYCLE*X_REGISTER
        SIGNAL_STRENGTHS.append(signal_strength)

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

print(f"END OF INSTRUCTIONS REACHED DURING CYCLE {CYCLE}")
print(f"FINAL X REGISTER VALUE: {X_REGISTER}")
print(SIGNAL_STRENGTHS)
print(sum(SIGNAL_STRENGTHS))