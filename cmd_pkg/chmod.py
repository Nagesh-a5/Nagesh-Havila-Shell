import os

"""
COMMAND NAME        :  chmod
DESCRIPTION         :  It is used to change modify permission.
"""

def chmod(perm, _f):
    octal = int('0o' + perm, 8)
    os.chmod(_f, octal)
