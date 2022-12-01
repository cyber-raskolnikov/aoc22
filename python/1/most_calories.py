with open("./python/1/input/first.txt", 'r') as file:
    elf_calories = [sum([int(calories_amount) for calories_amount in elf_calories.split('\n')]) for elf_calories in file.read().split('\n\n')]
    print(max(elf_calories))
