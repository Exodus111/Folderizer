Folderizer.

Folderizer is a python script that will categorize your downloaded television series into a library of subfolders.

It works in two steps, flatten and sort.

--flatten
    Will go through the root directory and look for subdirectories containing the pattern SxxExx. (Ex. S02E09)
    These folders will then be searched and any video files (.mp4, .mkv, .avi) will be extracted to root directory.
    These folders will then be deleted.

--sort
    Will go through all files in your main directory and gather those files fitting the pattern SxxExx and any files with numerical pattern. It then makes folder names out of these files, and moves every file to its proper folder.

Example of a typical usecase:

    python folderize.py --flatten
    python folderize.py --sort

Some more advanced features are also added, like setting your own directory and setting your own patterns.
