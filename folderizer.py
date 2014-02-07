"""
Folderizer.
This is a program to sort downloaded series files into individual folders.

This program does in no way condone illegal file downloading.
Downloading files illegally is immoral and WRONG, and can be punished by up to life in prison or the death penalty (depending on your state or country).
Illegal downloads steals the hard earned money of not only starving artists but most importantly hard working executive producers, who desire nothing but the well being of their audience, but thanks to illegal downloading, can barely survive in todays economy living only by sleeping on their friends couches and hitchhiking to work.

Use this program at your own discretion, I am in no way responsible for what you do with it, or how you chose to live your life, but call your mom dude... seriously.

This program is Open Source (GPLv3 license).
"""
import argparse
import re
from path import path

root = path(".")
SEpattern = "[Ss]\d+[Ee]\d"
NUMpattern = "[0-9]"
Videofiles = ["*.mkv", "*.mp4", "*.avi"]


def _find_pattern(names, pattern):
    #This function finds the correct files or folders following the SxxExx pattern.
    checked = {}
    for i in names:
        num = re.search(pattern, i.name)
        if num != None:
            checked[i] = num.start()
    return checked

def flatten(root, folder_pattern, file_pattern):
    #Here we empty and delete all relevant folders.
    folders = _find_pattern(root.dirs(), folder_pattern)
    for folder in folders:
        for p in file_pattern:
            for file in folder.walkfiles(p):
                path(file).move(root)
        folder.rmtree_p()

def sort(root, pattern):
    #Here we make our new folders and move all files from root to where they belong.
    checkedfiles = _find_pattern(root.files(), pattern)
    for file in checkedfiles:
        filename = str(file.basename())
        filename = filename[:checkedfiles[file]].rstrip(".")
        filename = filename.replace(".", " ")
        filename = filename.capitalize()
        folder = root / path(filename)
        folder.mkdir_p()
        file.move(folder)


#Argparse allows the user to input commands to our program in the CLI.
parser = argparse.ArgumentParser(prog="folderizer", description="Find all episode files and put them into their own folders. Requires the flatten argument to be run first then sort. The program looks for folders and files with the set pattern (currently set for video files), then categorises them into subfolders. Assumes root is the directory you are in, unless otherwise specified.")


parser.add_argument("-f", "--flatten",
                    action="store_const",
                    const="flatten",
                    dest="mode",
                    help="Flatten will go through subfolders that fit the pattern, move relevant files to root and delete the subfolders.")
parser.add_argument("-s", "--sort",
                    action="store_const",
                    const="sort",
                    dest="mode",
                    help="Sort find the files in the root directory and makes and/or moves them to their proper folders.")
parser.add_argument("-p", "--pattern",
                    action="count",
                    help="Allows you to set a new pattern for more advanced use. This is a counter and will require you input the neccesary variables. 1: Sets Main pattern. 2: Sets secondary pattern (Used to find files in subdirs). 3: Sets filenames")
parser.add_argument("varlist",
                    nargs="*",
                    help="Optionally you can specify a new root directory")

args = vars(parser.parse_args())

if args["varlist"] != []:
    if args["pattern"] == 0:
        root = path(args["varlist"][0])
        print "New Root directory set"
    if args["pattern"] >= 1:
        SEpattern = args["varlist"][0]
        print "New Main pattern set"
    if args["pattern"] >= 2:
        NUMpattern = args["varlist"][1]
        print "New Optional pattern set"
    if args["pattern"] >= 3:
        Videofiles = args["varlist"][2]
        print "New File pattern set"
    if args["pattern"] >= 4:
        root = args["varlist"][3]
        print "New Root Directory set"
if args["mode"] == "flatten":
    print "Flattening"
    flatten(root, SEpattern, Videofiles)
elif args["mode"] == "sort":
    print "Sorting"
    sort(root, SEpattern)
    sort(root, NUMpattern)
else:
    print "Incorrect Use. --help for more options"





