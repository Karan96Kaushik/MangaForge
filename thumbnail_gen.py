import os
import sys
import subprocess

def thumb_dir(directory): #thumbnails of complete directory
	mypath = directory

	try:
	    os.mkdir(mypath + '/thumbs/')
	except:
		print()
			
	for (dirpath, dirnames, filenames) in os.walk(mypath):
		print(filenames)
		for file in filenames:
			if(file.endswith('.mp4')):
				video_input_path = mypath + file
				img_output_path = mypath + '/thumbs/' + file + '.jpg'
				subprocess.call(['ffmpeg', '-i', video_input_path, '-ss', '00:00:10.000', '-vframes', '1', img_output_path])
		break

def thumb_curr(): #thumbnails of complete directory
	mypath = os.getcwd() + '/'

	try:
	    os.mkdir(mypath + 'thumbs/')
	except:
		print()
			
	for (dirpath, dirnames, filenames) in os.walk(mypath):
		print(filenames)
		for file in filenames:
			if(file.endswith('.mp4')):
				video_input_path = mypath + file
				img_output_path = mypath + 'thumbs/' + file + '.jpg'
				subprocess.call(['ffmpeg', '-i', video_input_path, '-ss', '00:00:10.000', '-vframes', '1', img_output_path])
		break
try:
    if(sys.argv[1] == 'current'):
        thumb_curr()
except:
    print()