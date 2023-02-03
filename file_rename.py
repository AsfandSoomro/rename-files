"""
    A program to rename all the files with provided extensions (by keeping the original files in the same folder and renaming in a new directory)
    Tips:
        - Use 'textract' library if you wanna open '.doc' or 'docx' files
"""

import os

# Address for files to work with and where those files saved after renaming
# Use extentions to provide what type of extension you want to work with
addr = './sample'
addr_r = './sample_renamed'
extensions = ('.txt', '.example')

# List of '.txt' files to work with
files = list()
for file in os.listdir(addr):
    if file.endswith(extensions):
        files.append(file)

# Creating a new directory for files renamed
try:
    os.mkdir(addr_r)
except FileExistsError:
    pass


# Iterating over each file
for file in files:
    name, ext = file.split('.')
    # Opening a file for reading
    with open(f'{addr}/{file}', 'r') as f:
        # Copying the contents of the file to the new file in new directory
        content = f.read()
        with open(f'{addr_r}/{name}_renamed.{ext}', 'w') as f_new:
            f_new.write(content)


