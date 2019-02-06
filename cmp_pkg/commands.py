#!/usr/bin/env python
from ls import ls
from pwd import pwd
from cat import cat
from grep import grep
from exit import exit
from history import history

class CommandsHelper(object):
    def __init__(self):
        self.invoke = {}
        self.help = {}

        for key, value in globals().items():
            if key != 'Commands' and callable(value):
                self.invoke[key] = value
                self.help[key] = value.__doc__

    def exists(self,cmd):
        return cmd in self.invoke
    
    def help(self,cmd):
        return self.commands.invoke[cmd].__doc__
    
        

if __name__=='__main__':
    pass