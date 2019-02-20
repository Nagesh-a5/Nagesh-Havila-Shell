import os
from os.path import expanduser


def cd(arg):
    if '~' in arg:
        arg = arg.replace('~', expanduser('~'))
    os.chdir(arg)
    return 'in ' + os.getcwd()
