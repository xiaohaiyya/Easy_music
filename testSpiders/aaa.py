
import os
dir_name = 'AAA'
if not os.path.isdir('img'):
    os.makedirs(dir_name)

dir_name = 'AAA/{}'.format(a)
if not os.path.isdir(dir_name):
    os.makedirs(dir_name)