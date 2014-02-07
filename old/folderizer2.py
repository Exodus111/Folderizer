"""
Folderizer 2
"""
import argparse
import re
from path import path

root = path("./Test")

def find_pattern(names):
    pattern = "S\d+E\d"
    checked = {}
    for i in names:
        num = re.search(pattern, i.basename())
        if num != None:
            checked[i] = num.start()
    return checked

def flatten(root):
    folders = find_pattern(root.dirs())
    for folder in folders:
        for files in folder.walkfiles():
            files = find_pattern([files])
            for file in files:
                path(file).move(root)
        folder.rmtree_p()

def sort(root):
    vidfiles = find_pattern(root.files())
    for file in vidfiles:
        filename = str(file.basename())
        filename = filename[:vidfiles[file]].rstrip(".")
        filename = filename.replace(".", " ")
        folder = root / path(filename)
        folder.mkdir_p()
        file.move(folder)


parser = argparse.ArgumentParser(description="Find all episode files and put them into their own folders. Requires the flatten argument to be run first then sort.")
parser.add_argument("-f", "--flatten", help="Check all subdirectories and move the relevant files to the root directory. Will delete all relevant subdirectories", action="store_true")
parser.add_argument("-s", "--sort", help="Sort all the files in the root directory, making and moving the relevant files to their own folders", action="store_true")

args = parser.parse_args()
if args.flatten:
    flatten(root)
elif args.sort:
    sort(root)
else:
    print "Please pick an option: --flatten, --sort"





