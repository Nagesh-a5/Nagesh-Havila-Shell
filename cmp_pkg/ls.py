#!/usr/bin/env python
from subprocess import call
from subprocess import check_output

def ls(**kwargs):
    return check_output(["ls",'.'], shell=True)


ls.__doc__="""
ls : Directory listing
"""
