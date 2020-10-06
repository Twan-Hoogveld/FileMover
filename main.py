import os
import sys
import time
import getpass

if __name__ == '__main__':
	#path to download folder
	path = "C:\\Users\\{}\\Downloads".format(getpass.getuser())

	#Get all the files
	files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))]

	#Get all the extensions from the files
	extensions = set()
	for file in files:
		extensions.add(file.split(".")[-1])

	#make directories from the extensions if not there yet
	dirList = os.listdir(path)
	for extension in extensions:
		if extension not in dirList:
			os.mkdir(os.path.join(path,extension))

	#move the files into the respectable folder.
	files01 = [i.split('.') for i in files]
	for i , file in enumerate(files01):
		oldPath = os.path.join(path,files[i])
		newPath = os.path.join(path,files01[i][-1],files[i])
		os.rename(oldPath,newPath)