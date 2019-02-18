import pydoc

"""
COMMAND NAME      :  less
DESCRIPTION       :  To display a file in a page at a time.
PARAMETERS        :  file
"""

def less(file):
    with open(file, 'r') as f:
        pydoc.pager(f.read())
