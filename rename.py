# -*- coding: UTF-8 -*-


import os, sys

# cdir = os.getcwd()
# print(cdir)
dir = os.listdir('dataset')

# dir.remove('rename.py')
# # print(dir)
for index, name in enumerate(dir):
    # print(name)
    os.rename('dataset/' + name, 'dataset/' + 'yokino_' + str(index + 1) + '.jpg')
print('Rename Success!')