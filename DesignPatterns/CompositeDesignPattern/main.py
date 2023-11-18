from directory import Directory
from file import File

# Creating a directory
root_directory = Directory("Root")

# Adding files to the root directory
file1 = File("File1.txt")
file2 = File("File2.txt")
root_directory.add(file1)
root_directory.add(file2)

# Creating a subdirectory
sub_directory = Directory("Subdirectory")

# Adding files to the subdirectory
file3 = File("File3.txt")
file4 = File("File4.txt")
sub_directory.add(file3)
sub_directory.add(file4)

# Adding the subdirectory to the root directory
root_directory.add(sub_directory)

# Displaying the entire file system
root_directory.ls()