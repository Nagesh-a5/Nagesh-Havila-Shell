import os
from os.path import expanduser
"""
COMMAND NAME   :   cd (change directory)
DESCRIPTION    :   Used to change directory to named directory.
        ~      :  Used to change directory to home directory.
       ..      :   Used to change directory to parent directory
PARAMETERS     :  Directory
"""

def cd(arg):
    if '~' in arg:
        arg = arg.replace('~', expanduser('~'))
    os.chdir(arg)
    return 'in ' + os.getcwd()
