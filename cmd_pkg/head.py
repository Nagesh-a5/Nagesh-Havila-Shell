"""
COMMAND NAME        :  head
DESCRIPTION         :  It is used to display the first few lines of the file.
PARAMETERS          :  file
"""
def head(file, num):
    n = num
    out = []
    with open(file, 'r') as _file:
        for _line in _file:
            if n == 0:
                break
            out.append(_line)
            n -= 1
    return ''.join(out)
