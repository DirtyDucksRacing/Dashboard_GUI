'''Daniel Craig'''
'''I PlEdGe My HoNoR tHaT i HaVe AbIdEd By ThE sTeVeNs HoNoR sYsTeM'''

from tkinter import *
import time
import random
import speedometer
import tachometer
from cv2 import *
from PIL import Image, ImageTk

WIDTH,HEIGHT=1024,576

'''Tkinter, initialize all variables'''

root=Tk()

#Video capture
video=cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH,300)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,200)

screen=Canvas(root,height=HEIGHT,width=WIDTH)
speedtext = Label(text="0")
rpmtext=Label(text='0',fg="black")
throttletext=Label(text='0')
speedtext.config(font=("Arial",60))
rpmtext.config(font=("Arial",60))
throttletext.config(font=("Arial",40))
speedtext.place(rely=0.9,relx=0.0,anchor='w')
rpmtext.place(rely=0.9,relx=1.0,anchor='e')
throttletext.place(relx=0.5,rely=0.15,anchor='n')
screen.pack()
screen.create_oval(30,30,300,300,tag="oval")
screen.create_oval(1000,30,720,310,tag="tachoval")
A=speedometer.Speedometer(screen,"oval",Range=(40,0))
B=tachometer.Tachometer(screen,"tachoval",Range=(7000,0))

#Label for camera spot
lmain=Label(root)
lmain.place(relx=0.5,rely=0.5,anchor='c')


#Week 1
'''
Camera in the center.
speedometer on the left
below speedometer -> Tachometer
Right side - digital number readout
left side - engine rpm. lower left - number. upper left - dial
right side - miles per hour. Lower right - number. Upper right - dial'''

#Week 2
'''
Try to get webcam feed
Or work on tachometer
Only show every other number to make it easier to read
'''

#Week 3
'''
Put webcam feed into tkinter window

Will eventually work on interfacing with arduino
'''

#Week 4
'''
Main focus:
    Fix speedometer
    Learn about serial communication

Other:
Log all of it to a csv file.
    As rpm is being displayed
    timestamp: engine speed, vehicle speed
    engine rpm as function of time
    
'''

releasedVideo=False
testSpeed=0
tachSpeed=0
def getSpeed(increment):
    return int(20+increment)

#def updateLabel(speedInput):      #Input for speed goes here
while(True):
    _, frame=video.read()
    frame=cv2.flip(frame,1)
    cv2image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    img=Image.fromarray(cv2image)
    imgtk=ImageTk.PhotoImage(image=img)
    lmain.imgtk=imgtk
    lmain.configure(image=imgtk)
    time.sleep(0.0333)
    speedtext.config(text=str(testSpeed)+' mph')
    rpmtext.config(text=str(tachSpeed)+" rpm")
    throttletext.config(text="Throttle: "+str(random.randint(0,100)))
    A.moveto(testSpeed,"oval")
    B.moveto(tachSpeed,"tachoval")
    screen.update()
    tachSpeed+=100
    testSpeed+=1

video.release()

screen.mainloop()
