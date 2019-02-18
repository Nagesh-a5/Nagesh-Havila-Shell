import shutil

"""
COMMAND NAME        :   mv  (move)
DESCRIPTION         :  It is used to move or rename the  file to the other file.
PARAMETERS          : file 1,file2.
"""

def mv(_from, to):
    shutil.move(_from, to)
    return _from + ' successfully moved'
