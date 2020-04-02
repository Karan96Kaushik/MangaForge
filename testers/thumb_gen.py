import subprocess
import os

mypathfol = os.getcwd() + '/Comix/'

for (dirpath, dirnames, filenames) in os.walk(mypathfol):
	for folder in dirnames:
		mypath = os.getcwd() + '/Comix/' + folder + '/'
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
	break
