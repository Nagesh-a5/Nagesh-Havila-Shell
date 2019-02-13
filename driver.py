# import sys
# sys.path.insert(0,'/cmd_pkg')
# from cmd_pkg import test 
# print("Hello world")
# input("% ")

# print(dir(test))

import threading
import time
import sys
import os
import shutil
import re
from cat import cat
from cp import cp
from mv import mv
from ls import ls

class Driver(object):
	def __init__(self):
		pass

    			
	def runShell(var1,pipe):
			
			var=var1.split(" ") 
								#splits the command into list
			command0=var[0]			#stores command in a variable
			
			
			occurance=var.count('>') #checking whether command has redirect ouput
			count=var.count('>>')  #checking whether command has to append ouput
		  
			input=var.count('<') #checking whether command has redirect input
			
			#Checks whether & exists to set daemon status
			daemoncount=var.count('&')
			if daemoncount == 1:
				daemonstatus="true"
			else:
				daemonstatus="false"


            elif command0 == 'ls' and occurance == 0 and count == 0:
				
				if len(var) == 1:
					l = threading.Thread(target=ls,args=(None,count,pipe,))
					
					l.start()
					if daemonstatus == 'false':
						l.join()
				else:
					command1=var[1]
					if command1 == '-l':  # calls ls -l
						l = threading.Thread(target=lsl,args=(None,count,pipe,))
						
						l.start()
						if daemonstatus == 'false':
							l.join()
					elif command1 == '-a': #calls ls -a
						l = threading.Thread(target=lsa,args=(None,count,pipe,))
						
						l.start()
						if daemonstatus == 'false':
							l.join()
					elif command1 == '-h':  #calls ls -h
						l = threading.Thread(target=lsh,args=(None,count,pipe,))
						l.start()
						if daemonstatus == 'false':
							l.join() 
					elif command1 == '-lh' or command1 == '-hl':
						l=threading.Thread(target=lslh,args=(None,count,pipe,))
						l.start()
						if daemonstatus == 'false':
							l.join()
					elif command1 == '-la' or command1 == '-al':
						l=threading.Thread(target=lsla,args=(None,count,pipe,))
						l.start()
						if daemonstatus == 'false':
							l.join()
					elif command1 == '-lah':
						
						l=threading.Thread(target=lslah,args=(None,count,pipe,))
						l.start()
						if daemonstatus == 'false':
							l.join()
					elif command1 == '-ah' or command1 == '-ha':
							l=threading.Thread(target=lsah,args=(None,count,pipe,))
							l.start()
							if daemonstatus == 'false':
								l.join()	

            elif command0 == 'mv':
				if len(var) == 1 or var[1].count('.') == 0 :
					print("Invalid command")
				else:
					command1=var[1]
					command2=var[2]
					c=threading.Thread(target=mv,args=(command1,command2,))
					c.start()
					if daemonstatus == 'false':
						c.join()
            


            elif occurance == 1 or count == 1:
            

            elif command0 == 'ls':
					if len(var) == 3:
						command1=var[2]
						c=threading.Thread(target=ls,args=(command1,count,pipe,))
						
						c.start()
						if daemonstatus == 'false':
							c.join()
					else:
						command1=var[1]
						command2=var[3]
						if command1 == '-l':  # calls ls -l
							l = threading.Thread(target=lsl,args=(command2,count,pipe,))
							
							l.start()
							if daemonstatus == 'false':
								l.join()
						elif command1 == '-a': #calls ls -a
							l = threading.Thread(target=lsa,args=(command2,count,pipe,))
							
							l.start()
							if daemonstatus == 'false':
								l.join()
						elif command1 == '-h':  #calls ls -h
							l = threading.Thread(target=lsh,args=(command2,count,pipe,))
							l.start()
							if daemonstatus == 'false':
								l.join() 
						elif command1 == '-lh' or command1 == 'hl':
							l=threading.Thread(target=lslh,args=(command2,count,pipe,))
							
							l.start()
							if daemonstatus == 'false':
								l.join()
						elif command1 == '-la' or command1 == 'al':
							l=threading.Thread(target=lsla,args=(command2,count,pipe,))
							
							l.start()
							if daemonstatus == 'false':
								l.join()
						elif command1 == '-lah':
							l=threading.Thread(target=lslah,args=(command2,count,pipe,))
							l.start()
							if daemonstatus == 'false':
								l.join()
						elif command1 == '-ah' or command1 == '-ha':
							l=threading.Thread(target=lsah,args=(command2,count,pipe,))
							l.start()
							if daemonstatus == 'false':
								l.join()
					
					
	def exit():
		raise SystemExit
		
		
	if __name__ == '__main__':
	
	
		#Asks input for entering commands to user till exiting from shell

		
		
		while True:
			print("\n")
			var=raw_input("%")  # takes input from shell
			if len(var) == 0:
				continue
			var1=var.split(" ")
			history(*var1)#command entered by user will be stored in history file   
			

			pipe=0
			
			#if piping to be implemented
			
			if '|' in var:
				commands=var.split("|")
				pipe=1
				if len(commands) == 2:
					firstcommand=commands[0]
					firstcommand=firstcommand.strip()
					
					runShell(firstcommand,pipe)
					pipe=0
					redirect=commands[1].count('>')
					append=commands[1].count('>>')
					if redirect == 0 and append == 0:
						secondcommand=commands[1]+'\t'+"pipe.txt"
						secondcommand=secondcommand.lstrip()
						secondcommand=' '.join(secondcommand.split())
						
						runShell(secondcommand,pipe)
					elif redirect == 1 :
						commandlist=commands[1].split(">")
						
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						
						runShell(passedcommand,pipe)
					elif append == 1:
						commandlist=commands[1].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">>"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)	
						
					
				elif len(commands) == 3:
					runShell(commands[0],pipe)
					
					secondcommand=commands[1]+'\t'+"pipe.txt"
					secondcommand=secondcommand.lstrip();
					secondcommand=' '.join(secondcommand.split())
					runShell(secondcommand,pipe)
					
					pipe=0
					redirect=commands[2].count('>')
					append=commands[2].count('>>')
					if redirect == 0 and append == 0:
						thirdcommand=commands[2]+'\t'+"pipe.txt"
						thirdcommand=thirdcommand.lstrip();
						thirdcommand=' '.join(thirdcommand.split())
						
						runShell(thirdcommand,pipe)
					elif redirect == 1:
						commandlist=commands[2].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)
						
					elif append == 1:
						commandlist=commands[2].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">>"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)
				
				elif len(commands) == 4:
					runShell(commands[0],pipe)
					secondcommand=commands[1]+'\t'+"pipe.txt"
					secondcommand=secondcommand.lstrip();
					secondcommand=' '.join(secondcommand.split())
					runShell(secondcommand,pipe)
					
					thirdcommand=commands[2]+'\t'+"pipe.txt"
					thirdcommand=thirdcommand.lstrip();
					thirdcommand=' '.join(thirdcommand.split())
					runShell(thirdcommand,pipe)
					redirect=commands[3].count('>')
					append=commands[3].count('>>')
					pipe=0
					if redirect == 0 and append == 0:
						fourthcommand=commands[3]+'\t'+"pipe.txt"
						fourthcommand=fourthcommand.lstrip();
						fourthcommand=' '.join(fourthcommand.split())
						runShell(fourthcommand,pipe)
					elif redirect == 1:
						commandlist=commands[3].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)
						
					elif append == 1:
						commandlist=commands[3].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">>"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)

				elif len(commands) == 5:
					runShell(commands[0],pipe)
					secondcommand=commands[1]+'\t'+"pipe.txt"
					secondcommand=secondcommand.lstrip();
					secondcommand=' '.join(secondcommand.split())
					runShell(secondcommand,pipe)
					
					thirdcommand=commands[2]+'\t'+"pipe.txt"
					thirdcommand=thirdcommand.lstrip();
					thirdcommand=' '.join(thirdcommand.split())
					runShell(thirdcommand,pipe)
					fourthcommand=commands[3]+'\t'+"pipe.txt"
					fourthcommand=fourthcommand.lstrip();
					fourthcommand=' '.join(fourthcommand.split())
					runShell(fourthcommand,pipe)
					
					
					redirect=commands[4].count('>')
					append=commands[4].count('>>')
					pipe=0
					if redirect == 0 and append == 0:
						fifthcommand=commands[4]+'\t'+"pipe.txt"
						fifthcommand=fifthcommand.lstrip();
						fifthcommand=' '.join(fifthcommand.split())
						runShell(fifthcommand,pipe)
					elif redirect == 1:
						commandlist=commands[4].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)
						
					elif append == 1:
						commandlist=commands[4].split(">")
						passedcommand=commandlist[0]+'\t'+"pipe.txt"+'\t'+">>"+"\t"+commandlist[1]
						passedcommand=passedcommand.lstrip();
						passedcommand=' '.join(passedcommand.split())
						runShell(passedcommand,pipe)
						
						
						
						
			
			#if command to be executed from history then..
			
			elif var[0] == '!':
				f=open("history.txt",'r')
				num=int(var[1:])
				num=num-1
				for i, line in enumerate(f):
					if i == num:
						var=line
						number=str(num)
						length=len(number)
						var1=var[length:]
						var1=var1.lstrip()
						var2=' '.join(var1.split())
						runShell(var2,pipe)
							
							
							
			#if entered command is exit				
			
			
			elif str.lower(var) == 'exit':
				exit()
				
			#if any commands entered ,then passed to runShell method as parameter	
			else:
				runShell(var,pipe)
			
	
		
                            