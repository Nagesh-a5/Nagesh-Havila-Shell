

"""
    Name: ls
    Description:
        lists files and directories
    Params: 
        file:if there is standard redirect output to file then filename is passed else None.
		count : checks whether output should append to file exists (>>)
		pipe : checking whether commands contains piping
    Returns: None
""" 

import os
def ls(file,count,pipe):
	path = '.'
	files = os.listdir(path)
	filelist=[]
	
	for name in files:
		filelist.append(name)
		
	filelist.sort()
	if pipe == 1:
		f1=open("pipe.txt",'w')
		for name in files:
			f1.write(name)
			f1.write("\n")
		f1.close()	
	else:		
		if count == 0 and file != None:
			f=open(file,'w')
		elif count == 1:
			f=open(file,'a')
			
			
			
		for content in filelist:
			if file == None:
				print(content+"\t")
			else:
				f.write(content)
				f.write("\n")


