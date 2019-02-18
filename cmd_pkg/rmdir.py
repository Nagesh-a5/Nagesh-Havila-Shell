import shutil

"""
COMMAND NAME      :  rmdir
DESCRIPTION       :  To remove the directory. 
PARAMETERS        :   Directory
"""

def rmdir(_dir):
    shutil.rmtree(_dir)
    return _dir + ' successfully removed'
