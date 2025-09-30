import tarfile #Moudle used to work with tar files

for i in range(999, 0, -1): #For loop from 999 to 0 going down by 1
	filename = str(i) + '.tar' #Get the name of the file
	#print(filename) - just for debug
	tar = tarfile.open(filename) #Open the file
	tar.extractall() #Extract what in the file
	tar.close() #Close the file
