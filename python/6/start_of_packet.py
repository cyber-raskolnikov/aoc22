import sys

LOOKUP_BUFFER_SIZE = 4

transmission = sys.stdin.read()

for position in range(LOOKUP_BUFFER_SIZE-1, len(transmission)):
    lookup_buffer = transmission[position-3:position+1]

    if len(set(lookup_buffer)) == LOOKUP_BUFFER_SIZE:
        print(f"START OF SEQUENCE FOUND: {lookup_buffer} AT POSITION {position+1}")
        quit()

    print(transmission[position-3:position+1])