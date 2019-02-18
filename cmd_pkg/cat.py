"""
COMMAND NAME      :  cat
DESCRIPTION       :  To display the given file.
PARAMETERS        :  file
"""

def cat(files):
    out = []
    for arg in files:
        with open(arg, 'r') as _file:
            for _line in _file:
                out.append(_line)
    return ''.join(out)
