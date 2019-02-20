"""
COMMAND NAME      :  wc (word count)
DESCRIPTION       :  It is used to count the words,lines and characters in a file.
PARAMETERS        :  file
"""
def wc(args, _l, _m, _w, from_pipe=False):
    out = []

    if from_pipe:
        args = ' '.join(args)
        if _l:
            size = args.count('\n') + 1
        elif _w:
            size = len(args.split(' '))
        else:
            size = len(args)
        return str(size)

    for _f in args:
        with open(_f) as o:
            if _l:
                size = len(o.readlines())
            elif _w:
                size = len(o.read().split(' '))
            else:
                size = len(o.read())
            out.append(_f + ' ' + str(size))
    return '\n'.join(out)
