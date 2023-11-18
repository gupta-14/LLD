from fileSystem import FileSystem

class File(FileSystem):
    def __init__(self, name) -> None:
        self.fileName = name

    def ls(self):
        print(f"filename : {self.fileName}")