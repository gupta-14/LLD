from fileSystem import FileSystem

class Directory(FileSystem):
    def __init__(self, name) -> None:
        self.directory_name = name
        self.file_system_list = []

    def add(self, file_system_obj):
        self.file_system_list.append(file_system_obj)

    def ls(self):
        print(f"Directory name : {self.directory_name}")
        for file_system_obj in self.file_system_list:
            file_system_obj.ls()