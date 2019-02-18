import linecache

import sys
"""
COMMAND NAME      :  tail
DESCRIPTION       :  It is used to display the last few lines of the file.
PARAMETERS        :  file
"""

def tail(file, num):
    n = num
    out = []
    tot_lines = len(open(file).readlines())
    for i in range(tot_lines - n + 1, tot_lines + 1):
        out.append(linecache.getline(file, i))
    return ''.join(out)
