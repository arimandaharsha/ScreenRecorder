import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

filename = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(filename, fourcc, 30.0, (width, height))
'''uncomment the commented code to display webcam'''
# webcam = cv2.VideoCapture(0)


while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    # _, frame = webcam.read()
    # frame_height, frame_width, i = frame.shape
    # img_final[0:frame_height, 0:frame_width, :] = frame[0:frame_height, 0:frame_width, :]
    cv2.imshow('Screen Recorder', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break
