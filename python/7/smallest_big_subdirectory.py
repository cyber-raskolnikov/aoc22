# working under the asumption that we are not going to cd into a not previously listed directory

import sys
OVER_THRESHOLD = []
DEVICE_MEMORY_SIZE = 70000000
NEEDED_MEMORY_SIZE = 30000000

class Directory():
    def __init__(self, name: str, parent: "Directory") -> None:
        self.name = name
        self.parent = parent if parent is not None else self
        self.content = {}
        self.file_size = 0 # the size of the actual files contained in it
        self.dir_sizes = 0 # the size of the files contained in the directories contained in them
    
    def add_file(self, command: str):
        size, name = command.split(' ')

        if name not in self.content:
            self.content[name] = int(size)
            self.file_size += int(size)

    def add_dir(self, command: str):
        name = command.split(' ')[1]
        
        if name not in self.content:
            new_directory = Directory(name=name, parent=self)
            self.content[name] = new_directory
    
    def compute_size(self, prefix: str) -> int:
        for content in self.content.values():
            if isinstance(content, Directory):
                self.dir_sizes += content.compute_size(prefix=prefix+'\t')
        self.total_size = self.file_size + self.dir_sizes
        print(f"{prefix} {self.name} : {self.total_size}")
        
        return self.total_size
    
    def find_over_threshold_dirs(self, threshold: int):
        for content in self.content.values():
            if isinstance(content, Directory):
                content.find_over_threshold_dirs(threshold=threshold)

        if self.total_size >= threshold:
            OVER_THRESHOLD.append(self.total_size)

root_directory = Directory(name = '/', parent=None)
current_directory = root_directory

while (command := sys.stdin.readline().rstrip()):
    if command == "$ cd /":
        print("Moving to root dir")
        current_directory = root_directory
    elif command == "$ cd ..":
        print("Moving one directory up")
        current_directory = current_directory.parent
    elif command.startswith("$ cd"):
        print(command)
        destination_directory = command.split(' ')[2]
        current_directory = current_directory.content[destination_directory]
    elif command == "$ ls":
        print("Start ls parsing")
    elif command.split(' ')[0].isnumeric():
        current_directory.add_file(command)
    elif command.split(' ')[0] == "dir":
        current_directory.add_dir(command)
    else:
        raise Exception(f"Parse Error: {command}")

root_size = root_directory.compute_size('')
root_directory.find_over_threshold_dirs(threshold=NEEDED_MEMORY_SIZE-DEVICE_MEMORY_SIZE+root_size)

print(sorted(OVER_THRESHOLD))