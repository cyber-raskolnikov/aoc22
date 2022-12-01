# To be executed from the repo root
import os

for day in range(1,32):
    print(f"Creating structure for day {day}")

    folder_path = f"./python/{day}/"

    os.makedirs(folder_path + "input")
    os.makedirs(folder_path + "out")

    with open(folder_path + "first.py", 'x') as first_file:
        first_file.write(f"# CODE FOR FIRST EXERCISE OF DAY {day}")
    
    with open(folder_path + "second.py", 'x') as second_file:
        second_file.write(f"# CODE FOR SECOND EXERCISE OF DAY {day}")
