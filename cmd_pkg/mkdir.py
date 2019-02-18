import os

"""
COMMAND NAME        :    mkdir
DESCRIPTION         :    To create a directory.
PARAMETERS          :    Directory name
"""

def mkdir(dirs):
    out = []
    for arg in dirs:
        os.makedirs(arg)
        out.append(arg + ' created')
    return '\n'.join(out)
