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

#This function finds the correct files or folders following the SxxExx pattern.
def _find_pattern(names, pattern):
    checked = {}
    for i in names:
        num = re.search(pattern, i.name)
        if num != None:
            checked[i] = num.start()
    return checked

#Here we empty and delete all relevant folders.
def flatten(root, folder_pattern, file_pattern):
    folders = _find_pattern(root.dirs(), folder_pattern)
    for folder in folders:
        for p in file_pattern:
            for file in folder.walkfiles(p):
                path(file).move(root)
        folder.rmtree_p()

#Here we make our new folders and move all files from root to where they belong.
def sort(root, pattern):
    vidfiles = _find_pattern(root.files(), pattern)
    for file in vidfiles:
        filename = str(file.basename())
        filename = filename[:vidfiles[file]].rstrip(".")
        filename = filename.replace(".", " ")
        filename = filename.capitalize()
        folder = root / path(filename)
        folder.mkdir_p()
        file.move(folder)


#Argparse allows the user to input commands to our program in the CLI.
parser = argparse.ArgumentParser(prog="folderizer", description="Find all episode files and put them into their own folders. Requires the flatten argument to be run first then sort. The program looks for folders and files with the set pattern (currently set for video files), then categorises them into subfolders. Assumes root is the directory you are in, unless otherwise specified.")


parser.add_argument("-f", "--flatten",
                    action="store_true",
                    help="Flatten will go through subfolders that fit the pattern, move relevant files to root and delete the subfolders.")
parser.add_argument("-s", "--sort",
                    action="store_true",
                    help="Sort find the files in the root directory and makes and/or moves them to their proper folders.")
parser.add_argument("directory",
                    nargs="?",
                    default=None,
                    help="Optionally you can specify a new root directory")

args = vars(parser.parse_args())

if args["directory"] != None:
    root = path(args["directory"])
if args["flatten"] == True and args["sort"] == False:
    flatten(root, SEpattern, Videofiles)
elif args["sort"] == True and args["flatten"] == False:
    sort(root, SEpattern)
    sort(root, NUMpattern)
else:
    print "Incorrect Use. --help for more options"


