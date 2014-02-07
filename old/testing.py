import sys
import re
from path import path

def file_to_folder(file):
    regex = r'(.*)\b[Ss][0-9]+[Ee][0-9]+'
    filebase = file.basename().replace('.', ' ')
    folderbase = re.match(regex, filebase).group(1)
    return file.dirname() / folderbase

def flatten(root):
    for folder in root.dirs():
        for file in folder.walkfiles():
            file.move(root)
        folder.removedirs_p()

def categorise(root):
    for file in root.files():
        folder = file_to_folder(file)
        folder.mkdir_p()
        file.move(folder)

root = path("./Test")
categorise(root)

"""
if __name__ == '__main__':
    root = path('./Test')
    if '--flatten' in sys.argv:
        flatten(root)
    else:
        categorise(root)
"""
