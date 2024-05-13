import os
import subprocess
import pathlib
from pathlib import Path
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

fileInputFormat=[('All Image Format','*.TIFF; *.EXR; *.JPEG; *.SG; *.TGA; *.MayaIFF; *.DPX; *.BMP; *.HDR; *.PNG; *.GIF; *.PPM; *.XPM; *.Pixar; *.TEX; *.Z-files' ), 
				('PNG','*PNG'), ('EXR', '*.EXR'), ('JPEG','*.JPG *.JPEG'), ('TEX','*.TX *.TEX'), ('TARGA','*.TGA'), 
				('MayaIFF','*.MayaIFF'), ('GIF','*.GIF'),('HDR','*.HDR'),('BMP','*.BMP')]

command = 'txmake'
#extras = '' #for advanced mode in the future


def txMake(inputF, outputF, textBox):
	inputF_path = os.path.normpath(inputF.get())

	if inputF.get() == '':  #TXMake in case directory wasnt selected
		print('no file or directory')
		textBox.insert('end','no file or directory \n')
		return

	elif os.path.isfile(inputF_path): #txMake in case is a file
		if os.path.isdir(outputF.get()) == True:
			print('output folder doesnt exist, please check and retry')
			textBox.insert('end','output folder doesnt exist, please check and retry \n')
			return
		try:
			os.system(command + ' ' + inputF.get() + ' ' + outputF.get())
		except:
			print('Error when running txMake')
			textBox.insert('end','Error when running txMake \n')
			return

		print('File created at: ' + outputF.get())
		textBox.insert('end','File created at: ' + outputF.get() + '\n')
		clear(inputF, outputF)
		return

	elif os.path.isdir(inputF_path): #txMake in case is a directory
		listDir = os.listdir(inputF_path)
		texPath = createDirectory(inputF)
		textBox.insert('end', '\n created tex directory')
		for file in listDir:
			originalPath = inputF_path + '/' + file
			originalPath = os.path.normpath(originalPath)
			output = str(texPath) + '/' + file+'.tex'
			output = os.path.normpath(output)
			try:
				os.system(command + ' ' + originalPath + ' ' + output)
				textBox.insert('end', '\n converted ' + file + ' in: ' + output)

			except:
				print('Error when running txMake')
				textBox.insert('end', 'Error when running txMake \n possibly unsupported file for: ' + originalPath)
				return


	else:
		print('Directory or File not found')
		


def clear(inputF, outputF):
    inputF.delete(0, 'end')
    inputF.configure(placeholder_text='Images Directory')
    outputF.delete(0, 'end')
    outputF.configure(placeholder_text ='TEX Directory')

def createDirectory(inputF):
	path = os.path.join(inputF.get(), 'tex')
	try:
		os.mkdir(path)
		return path
	except:
		print('tex directory already exists, skipping step')
		return path 



def getDirectory(inputF, outputF): #Gets the directory and sets the path with a /tex/ output
	clear(inputF,outputF)
	directory = filedialog.askdirectory()
	if(directory == ''):
	    return
	else:
	    inputF.insert(0, directory)
	    outputF.insert(0, str(directory)+'/tex/')


def getFile(inputF, outputF):  #Gets the file and opens the file input
	clear(inputF,outputF)
	directory = askopenfilename(filetypes=fileInputFormat)
	if(directory == ''):
	    return
	else:
	    inputF.insert(0, directory)
	    outputF.insert(0, str(directory)+'.tex') 

