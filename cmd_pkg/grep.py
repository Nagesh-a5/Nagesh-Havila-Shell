import re

"""
COMMAND NAME :  grep
DESCRIPTION         :  It is used to search the given keyword from the file.
PARAMETERS          :  ‘keyword’ file
"""

def grep(pattern, files, _l):
    out = []
    for fname in files:
        found = False
        with open(fname, 'r') as f:
            count = 0
            for line in f:  
                if re.search(pattern, line):
                    count += 1
                    if _l:
                        found = True
                    
            if found:
                out.append(fname + '\n')
                out.append(str(count) + ' ')
                
    return ''.join(out)
