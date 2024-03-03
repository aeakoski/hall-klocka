# use Tkinter to show a digital clock
# tested with Python24    vegaseat    10sep2006
# https://www.daniweb.com/software-development/python/code/216785/tkinter-digital-clock-python
# http://en.sharejs.com/python/19617

# Anders E. Wallin, 2015-04-24
# GPLv3 license.
#
# added: UTC, localtime, date, MJD, DOY, week
import sys
if sys.version_info[0] == 3:
    from tkinter import *
else:
    from Tkinter import *
import time
import datetime
import math
from PIL import ImageTk, Image
import os

#import jdutil # https://gist.github.com/jiffyclub/1294443
#import gpstime

root = Tk()
root.attributes("-fullscreen", True)
# this should make Esc exit fullscrreen, but doesn't seem to work..
#root.bind('<Escape>',root.attributes("-fullscreen", False))
root.configure(background='black')

#root.geometry("1280x1024") # set explicitly window size
scale=0.8 # scale all fonts
time1 = ''

spacer = Label(root, height=10, bg='black', width=70 )
spacer.pack()

canvas = Canvas(root, width = 300, height = 300, bd=0, highlightthickness=0, relief='ridge', bg='black')
canvas.pack()
img = ImageTk.PhotoImage(Image.open("hall.png").resize((300, 300),Image.ANTIALIAS))
canvas.create_image(0, 0, anchor=NW, image=img)

clock_lt = Label(root, font=('arial', int(scale*230), 'bold'), fg='white',bg='black')
clock_lt.pack()

date_iso = Label(root, font=('arial', int(scale*75), 'bold'), fg='white',bg='black')
date_iso.pack()

date_etc = Label(root, font=('arial', int(scale*40), 'bold'), fg='white',bg='black')
date_etc.pack()

#clock_utc = Label(root, font=('arial', int(scale*230), 'bold'),fg='red', bg='black')
#clock_utc.pack()

#clock_gps = Label(root, font=('arial', int(scale*40), 'bold'),fg='red', bg='black')
#clock_gps.pack()

#clock_tai = Label(root, font=('arial', int(scale*40), 'bold'),fg='red', bg='black')
#clock_tai.pack()

def tick():
    global time1

    dt =datetime.datetime.utcnow()
    #time2 = time.strftime('%H:%M:%S') # local
    time2 = time.strftime('%H:%M') # local

    date_iso_txt = time.strftime('%Y-%m-%d', time.localtime())
    # day, DOY, week
    date_etc_txt = "%s   DOY: %s  Week: %s" % (time.strftime('%A'), time.strftime('%j'), time.strftime('%W'))

    if time2 != time1: # if time string has changed, update it
        time1 = time2
        clock_lt.config(text=time2)
        date_iso.config(text=date_iso_txt)
        date_etc.config(text=date_etc_txt)


    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock_lt.after(20, tick)

root.bind("x", quit)
tick()
root.mainloop()
