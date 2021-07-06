# -*- coding: UTF-8 -*-

# You can change the name of img by this file to meet your requests
import os, sys

# cdir = os.getcwd()
# print(cdir)
dir = os.listdir()
dir.remove('rename.py')
# print(dir)
for index, name in enumerate(dir):
    # print(name)
    os.rename(name, 'yokino_' + str(index + 1) + '.jpg')
print('Rename Success!')