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
                count += 1
                if re.search(pattern, line):
                    if _l:
                        found = True
                        break
                    out.append(str(count) + ' ' + line)
            if found:
                out.append(fname + '\n')
    return ''.join(out)
