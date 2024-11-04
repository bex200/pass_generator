def open_file_read_with():
    """Opens a file for a reading, file must exist"""
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

open_file_read_with()

def open_file_write_with():
    """Opens a file for a reading, file must exist"""
    with open("example.txt", "w") as file:
        file.write("this is a new file.\n")

