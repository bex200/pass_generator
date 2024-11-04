# Open the file
def open_file_read():
    """Opens a file for a reading"""
    file = open("example.txt", "r") # Open for reading - r, сперва путь потом метод обработки настройки
    content = file.read() # read the inside of the file
    print(content) # Displays the content of the document
    file.close()

open_file_read() #File must exist

# Mode of file openings
# "r" (read)- reading mode
# "w" (write)- writing mode, (creates if file does not exist, clears it if it already exists)
# "a" (append)- adds (adds data to the end of the file)
# "r+" (read and write)- read and write

def open_file_write():
    """Opens a file for editing writing and deleted previous what we have, creates file if it doesn't exist"""
    file = open("example.txt", "w") # It clears the previous data
    file.write("Add something more.\n") # Adding new data to file
    file.close()

open_file_write()

def open_file_append(message):
    """Opens a file foe eadding, creates if file does not exist"""
    file = open("example.txt", "a")
    file.write(f"\n{message}.\n")
    file.close()

open_file_append("I have a girlfriend")

def open_file_read_write():
    """Opens a file for a reading and editing. File must exist"""
    file = open("example.txt", "r+")
    content = file.read() # opens for reading
    print("Content of the file before editing:", content)
    file.write("Written content of R+.\n")
    file.close()

open_file_read_write()
