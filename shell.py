#!/usr/bin/env python
from cmd_pkg import commands 
import threading
import sys
from subprocess import call # for demo purposes only

def run_command(cmd,args=None,flags=None):

    if args:
        c = threading.Thread(target=cmd, args=(args,))
    else:
        c = threading.Thread(target=cmd)
        
    c.start()
    c.join()

def cat(file):
    call(["cat", file])


def ls():
    pass

def pwd():
    pass


if __name__ == '__main__':

    # if len(sys.argv) < 2:
    #     print("usage: python driver.py cmd where cmd = 'ls' or 'pwd', etc.")
    #     sys.exit(0)
 
    # cmd = sys.argv[1]
    
    # if cmd == 'ls':
    #     run_command(commands.ls,sys.argv[2])
    # elif cmd == 'pwd':
    #     run_command(commands.pwd)
    # elif cmd == 'cat':
    #     run_command(commands.cat,sys.argv[2])

    while True:
        cmd = raw_input('% ')
        cmd = cmd.split()
        
        if cmd[0] == 'cat':
            cat(cmd[1])
            print()
        elif cmd[0] == 'grep':
            if(len(cmd) < 3):
                run_command(commands.grepusage)
            else:
                run_command(commands.grep,cmd[1],cmd[2])
                #commands.grep(cmd[1],cmd[2])

        if cmd[0] == 'exit':
            break