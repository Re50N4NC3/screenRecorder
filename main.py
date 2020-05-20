import pyautogui as pgui
import time
from tkinter import Tk, Label, Button, messagebox


# capture screenshots to the array
def record(fps_in, area):
    for i in range(0, 80):
        fps_div = 1 / fps_in  # fps when input is in seconds
        start_time = time.time()
        ss = pgui.screenshot(region=area)  # take a screenshot
        frames.append(ss)
        time.sleep(fps_div - ((time.time() - start_time) % fps_div))
    frames[0].save(outputName, format='GIF', append_images=frames[1:], save_all=True, duration=fps, loop=0)


# save gif (source array, save path)
def save(arr, path):
    frames[0].save(path, format='GIF', append_images=arr[1:], save_all=True, duration=fps, loop=0)


# SETUP
resolution = pgui.size()  # assign native screen resolution

# Vars that can be changed by the user
outputName = "C:/Users/Tyst/Desktop/ScreenToGif/name.gif"  # +.gif
fps = 60.0  # Frapes Per Second
recLen = 60  # recording length
boundingBox = (0, 0, resolution[0], resolution[1])  # x1, y1, x2, y2

frames = []  # captured frames array

# GUI
win = Tk()
win.title("Screen recorder")

win.geometry("%dx%d+0+0" % (100, 100))
btnStart = Button(win, width=10, height=1, text='START', command= lambda: record(recLen, boundingBox))
# btnStop = Button(win, width=10, height=1, text='STOP', command=stop_capture)
btnStart.pack()
# btnStop.pack()

win.mainloop()
