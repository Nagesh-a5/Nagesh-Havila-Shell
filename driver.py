#!/usr/bin/env python3
"""
Program Name: SHELL COMMANDS
Team: Sai Nagesh Vadlani, Havila Pamidi
Description: 
	Implementation of "SHELL" in Python using the threads inorder to execute the each command in a thread.
"""
import cmd
import argparse
import multiprocessing as mp
from os.path import dirname, realpath
import sys
sys.path.append(dirname(realpath(__file__)))

from cmd_pkg import (
    ls, mkdir, pwd, cd, cp, mv, rm, rmdir, cat, less,
    head, tail, grep, wc, sort, who, chmod
)


def make_parser(args, flags, name='files'):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(name, metavar='N', type=str, nargs=argparse.REMAINDER)
    for flag in flags:
        parser.add_argument('-' + flag, action='store_true')
    parsed = parser.parse_args(args)
    return parsed


def wrap(f):
    def _wrapped(*args):
        _self = args[0]
        rest = args[1]
        if '--help' in rest:
            print(f.__doc__)
            return

        background = rest.endswith('&')
        arguments = args
        second = None
        second_type = None
        for sep in ['|', '>>', '>', '<']:
            if sep in rest:
                first, second = rest.split(sep)
                arguments = (_self, first)
                # remove trailing whitespaces
                second = second.replace(' ', '')
                second_type = sep
                break

        #def _fn(second, second_type, arguments):
        #    out = f(*arguments)
        #    if second is None:
        #        print(out)
        #    else:
        #        #if second_type == '|':
        #        #    _self.onecmd(second + ' ' + out)
        #        if second_type == '>':
        #            with open(second, 'w') as o:
        #                o.write(out)
        #        elif second_type == '>>':
        #            with open(second, 'a') as o:
        #                o.write(out)
        #        elif second_type == '<':
        #            inp = open(second).read()
        #            print(f(_self, inp))
        #    return

        print(f(*arguments))
        _self.hist.append(f.__name__[3:] + ' ' + rest)
    return _wrapped


class Shell(cmd.Cmd):
    intro = 'Type help or ? to list commands. Type exit to exit.\n'
    prompt = '% '

    def __init__(self):
        super().__init__()
        self.hist = []

    @wrap
    def do_ls(self, args):
        """
        list files and directories
        usage: ls [-h] [-l] [-a] [--help] files1 ... file2

        optional arguments:
        --help  show this help message and exit
        -a      list all show hidden files
        -h      human readable sizes
        -l      long listing
        """

        if args == '':
            args = '.'
        args = args.split()
        if args[-1].startswith('-'):
            args.append('.')
        parsed = make_parser(args, ['l', 'h', 'a'], name='dirs')
        return ls(parsed.dirs, parsed.h, parsed.a, parsed.l)

    @wrap
    def do_mkdir(self, args):
        """
        make a directory
        usage: mkdir dirname
        """
        return mkdir(args.split())

    @wrap
    def do_pwd(self, args):
        """
        display the path of the current directory
        usage: pwd
        """
        return pwd()

    @wrap
    def do_cd(self, arg):
        """
        change to a directory
        usage: cd directory
        if directory is
        ~  change to home-directory
        .. change to parent directory
        """
        return cd(arg)

    @wrap
    def do_cp(self, args):
        """
        copy file1 and call it file2
        usage: cp file1 file2
        """
        args = args.split()
        if len(args) > 2:
            return 'max 2 args'
        _from = args[0]
        to = args[1]
        return cp(_from, to)

    @wrap
    def do_mv(self, args):
        """
        move or rename file1 to file2
        usage: mv file1 file2
        """
        args = args.split()
        if len(args) > 2:
            return 'max 2 args'
        _from = args[0]
        to = args[1]
        return mv(_from, to)

    @wrap
    def do_rm(self, args):
        """
        remove a file
        usage: rm [-r] file
        if file has a wildcard, removes files that matches that wildcard

        optional arguments:
        -r recurses into non-empty folder to delete all
        """
        # TODO -r
        args = args.split()
        parsed = make_parser(args, ['r'])
        return rm(parsed.files, parsed.r)

    @wrap
    def do_rmdir(self, arg):
        """
        remove a directory
        usage: rmdir directory
        """
        return rmdir(arg)

    @wrap
    def do_cat(self, args):
        """
        display a file or multiple files concatenated
        usage: cat file1 file2 ... fileN
        """
        return cat(args.split())

    @wrap
    def do_less(self, arg):
        """
        display a file a page at a time
        usage: less file
        """
        less(arg)

    @wrap
    def do_head(self, args):
        """
        display the first few lines of a file
        usage: head [-n c] file

        optional arguments:
        -n c how many lines to display
        """
        arg = args
        n = 10
        if '-n' in args:
            _, nstr, arg = args.split()
            n = int(nstr)
        return head(arg, n)

    @wrap
    def do_tail(self, args):
        """
        display the last few lines of a file
        usage: head [-n c] file

        optional arguments:
        -n c how many lines to display
        """
        arg = args
        n = 10
        if '-n' in args:
            _, nstr, arg = args.split()
            n = int(nstr)

        return tail(arg, n)

    @wrap
    def do_grep(self, args):
        """
        search file(s) for keywords and print lines where pattern is found
        usage: grep [-l] 'keyword' file1 file2 ... fileN

        optional arguments:
        -l only return file names where the word or pattern is found
        """
        args = args.split()
        parsed = make_parser(args, ['l'])
        pattern = parsed.files[0]
        return grep(pattern, parsed.files[1:], parsed.l)

    @wrap
    def do_wc(self, args):
        """
        count number of lines/words/characters in file
        usage: wc [-l] [-m] [-w] file

        optional arguments:
        -l count number of lines in file
        -m count number of characters in file
        -w count number of words in file
        """
        args = args.split()
        parsed = make_parser(args, ['l', 'm', 'w'])
        return wc(parsed.files, parsed.l, parsed.m, parsed.w)

    @wrap
    def do_sort(self, args):
        """
        sort data
        usage: sort data
        """
        return sort(args)

    @wrap
    def do_who(self, args):
        """
        list users currently logged in
        usage: who
        """
        return who()

    @wrap
    def do_chmod(self, args):
        """
        change modify permission
        usage: chmod xxx file
        """
        args = args.split()
        if len(args) > 2:
            return 'only 2 args max'
        perm, _f = args
        chmod(perm, _f)
# """
# COMMAND NAME 	  :  history
# DESCRIPTION       :  It is used to show history of all commands in the file.
# """
    @wrap
    def do_history(self, args):
        return '\n'.join(self.hist)

    def do_shell(self, args):
        # For command starting with !
        cmd = self.hist[int(args)]
        print(cmd)
        self.onecmd(cmd)

    def do_exit(self, args):
        exit()


if __name__ == '__main__':
    Shell().cmdloop()
