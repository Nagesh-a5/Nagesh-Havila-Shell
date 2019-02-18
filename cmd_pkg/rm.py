import os
import shutil
from pathlib import Path

"""
COMMAND NAME      :  rm  (remove)
DESCRIPTION       :  To remove the file from directory.
PARAMETERS        :  file
"""


def rm(files, _r):
    for file in files:
        if _r and os.path.isdir(file):
            shutil.rmtree(file)
            continue
        for p in Path(".").glob(file):
            p.unlink()
    return ''
