# -*- coding: utf-8 -*-
import cv2
import numpy as np

#获得视频的格式
videoCapture = cv2.VideoCapture('./wo.mp4')

fps = videoCapture.get(cv2.CAP_PROP_FPS)
x = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
y = int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
imgsize = (x,y)
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
ooo = cv2.VideoWriter('./1.mp4',fourcc,fps,imgsize)


for x in range(1769):
	success, frame = videoCapture.read()
	frame_data = np.array(frame)
	for i in range(y):
		frame_data[i] = frame_data[i][::-1]
	#cv2.imshow('windows', frame_data) 
	#cv2.waitKey(1000/int(fps))
	#print(frame_data)
	ooo.write(frame_data)


#videoCapture.release()

