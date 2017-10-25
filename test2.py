import cv2
import numpy as np
import Tkinter 
from PIL import Image, ImageTk
import time

def start_tracking():
	cap = cv2.VideoCapture(0)
	cap2 = cv2.VideoCapture(1)
	stitcher = cv2.createStitcher(False)
	i=0
	window = Tkinter.Tk()
	window.title("Join")
	window.geometry("550x100")
	window.configure(background='grey')
	count = 0
	while True:
		i=i+1
		ret, frame = cap.read()
		ret1, frame1 = cap2.read()
		img = frame.copy()
		img2= frame1.copy()
		cv2.imshow('Image',img)
		cv2.imshow('Image2',img2)
		if(i%7 == 0):
			name = "frame_01.jpg"
			cv2.imwrite(name, frame)
			name1 = "frame_02.jpg"
			cv2.imwrite(name1, frame1)
			foo = cv2.imread(name)
			bar = cv2.imread(name1)
			result = stitcher.stitch((foo,bar))
			name3 = "result_%d.jpg"%i
			cv2.imwrite(name3, result[1])
			img_final = cv2.imread(name3)
			NULL = None 
			if(img_final != NULL):
				cv2.imshow('Panorama',img_final)
			else :
				print ('Frame number -> Missed frames' )
				count = count + 1
				print (i , count)
			
		c = cv2.waitKey(1)
		if(c == 27):
			break

	

if __name__ == '__main__':
        start_tracking()
        cv2.destroyAllWindows()

