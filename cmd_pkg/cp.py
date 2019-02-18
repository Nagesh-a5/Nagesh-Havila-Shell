import shutil

"""
COMMAND NAME :   cp (copy)
DESCRIPTION         :  It is used to copy the information from one file to the other file.
PARAMETERS         :   file1,file2
"""

def cp(_from, to):
    shutil.copyfile(_from, to)
    return to + ' successfully copied'
