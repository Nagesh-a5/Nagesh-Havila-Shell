import os
import stat

"""
COMMAND NAME             :  ls
DESCRIPTION              :   List  all files from the current directory.
	    -a               :    It shows all the hidden files.
	    -l               :    Displays  long listing.
        -h               :    Human readable sizes
"""


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def ls(dirs, _h, _a, _l):
    out = []

    def get_stat(path):
        filestat = os.stat(path)
        fsize = os.path.getsize(path)
        if _h:
            fsize = sizeof_fmt(fsize)
        return ' '.join([stat.filemode(filestat.st_mode), str(fsize), f])

    for arg in dirs:
        out.append(arg + ':')
        files = os.listdir(arg)
        for f in files:
            if _a and f.startswith('.'):
                # Skip hidden files
                continue
            if _l:
                path = os.path.join(arg, f)
                out.append(get_stat(path))
            else:
                out.append(f)
    return '\n'.join(out)
