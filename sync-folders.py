from dirsync import sync

sourcedir = '/media/rakib/files/test'
targetdir = '/media/rakib/files/test1'

sync(sourcedir, targetdir, 'sync')

# this script can sync 2 differnet folders, if any file is missing in the targeted folder then it will copy the file
# from the destination folder.