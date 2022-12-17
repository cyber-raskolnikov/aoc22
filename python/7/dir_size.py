# working under the asumption that we are not going to cd into a not previously listed directory

import sys

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