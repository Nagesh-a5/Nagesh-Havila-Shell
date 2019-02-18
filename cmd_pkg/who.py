import os

"""
COMMAND NAME    :  who
DESCRIPTION     :  It is used to list the users currently logged in.
"""

def who():
    return os.popen('who').read()
