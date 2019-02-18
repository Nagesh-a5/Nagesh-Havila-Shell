import os
"""
COMMAND NAME   :   cd (change directory)
DESCRIPTION    :   Used to change directory to named directory.
        ~      :  Used to change directory to home directory.
       ..      :   Used to change directory to parent directory
PARAMETERS     :  Directory
"""

def cd(arg):
    os.chdir(arg)
    return 'in ' + os.getcwd()
