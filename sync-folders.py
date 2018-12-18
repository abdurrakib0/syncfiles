from dirsync import sync

sourcedir = '/media/rakib/files/test'
targetdir = '/media/rakib/files/test1'

sync(sourcedir, targetdir, 'sync')

# file = open('/media/rakib/files/test/test.txt', 'r')
# print(file.read())