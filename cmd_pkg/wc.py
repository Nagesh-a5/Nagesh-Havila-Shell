"""
COMMAND NAME      :  wc (word count)
DESCRIPTION       :  It is used to count the words,lines and characters in a file.
PARAMETERS        :  file
"""

def wc(files, _l, _m, _w):
    out = []
    for _f in files:
        with open(_f) as o:
            if _l:
                size = len(o.readlines())
            elif _w:
                size = len(o.read().split(' '))
            else:
                size = len(o.read())
            out.append(_f + ' ' + str(size))
    return '\n'.join(out)
