#!/usr/bin/env python2
"""
This is a program to sort downloaded series files into individual folders.

This program does in no way condone illegal file downloading.
Downloading files illegally is immoral and WRONG, and can be punished by up to life in prison or the death penalty (depending on your state or country).
Illegal downloads steals the hard earned money of not only starving artists but most importantly hard working executive producers, who desire nothing but the well being of their audience, but thanks to illegal downloading, can barely survive in todays economy living only by sleeping on their friends couches and hitchhiking to work.

Use this program at your own discretion, I am in no way responsible for what you do with it, or how you chose to live your life, but call your mom dude... seriously.

This program is Open Source (GPLv3 license).
"""
#Path.py is a depency that needs to be installed
#You can find it at https://pypi.python.org/pypi/path.py
from path import path

#Here I set up the variables necesary to run the program
#the path here is set for whatever path the file happens to be in
my_folder = path("./")

# mode 1 checks, empties and removes all the downloaded folders
# mode 2 goes through the main folder and makes folders out of every series title
mode = 2

# This function checks the files in a folder or subfolders for the SxxExx tag.(ex.S01E01)
def read_dir(pathlist):
    namesdict = {}
    for i in pathlist:
        i = i.basename()
        check = i.find("S")
        while check != -1:
            if i[check+3] == "E" and not i[check+1] == "H":
                namesdict[i] = check
                check = -1
            else:
                check = i.find("S", check+1)
    return namesdict

# Here we make our folders
def make_dirs(folders):
    for t in folders:
        new_folder = my_folder + ("/" + t)
        new_folder.mkdir_p()
        folderlist.append(new_folder)

# Here we move the files
def move_files(my_dict):
    for newfolder in folderlist:
        folderstring = str(newfolder.basename())
        folderstring = folderstring.replace(" ", ".")
        for files in my_dict:
            if folderstring in files:
                newfile = my_folder + ("/" + files)
                newfile.move(newfolder)

# Here we read our subfolders, find the relevant ones,
# and move the relevant files out of it.
# Then delete the subfolder, all other files and all subsubfolders will be lost.
def check_dirs(path):
    my_dict = read_dir(path.dirs())
    for dirs in my_dict.keys():
        newdir = my_folder + ("/" + dirs)
        d = read_dir(newdir.files())
        for files in d.keys():
            newfile = my_folder + ("/" + dirs) + ("/" + files)
            newfile.move(my_folder)
        dirs = my_folder + ("/" + dirs)
        dirs.rmtree(ignore_errors=True)

# Here we read throguh all the files in the main folder.
# Take the relevant ones and format their names to make subfolders out of them.
def run_program():
    filesdict = read_dir(my_folder.files())
    for t in filesdict.keys():
        name = str(t)
        name = name[:filesdict[t]]
        name = name.replace(".", " ")
        name = name.rstrip()
        fileslist.append(name)
    fileslist2 = list(set(fileslist))
    make_dirs(fileslist2)
    move_files(filesdict)

# Neccesary Globals
fileslist = []
folderlist = []

# This runs everything, depending on the mode set.
if mode == 1:
    check_dirs(my_folder)
else:
    run_program()
