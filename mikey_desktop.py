#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mikeydesktop.py
#  
#  

def main(args):
    return 0

if __name__ == '__main__':
    import sys
import pyautogui
import random
import tkinter as tk
x = 100 #Mikey's x position
y = 0 #Mikey's y position
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = 'C:/PATHWAYHERE'
#transfer random no. to event
def event(cycle,check,event_number,x):
 if event_number in idle_num:
  check = 0
  print('idle')
  window.after(400,update,cycle,check,event_number,x) #no. 1,2,3,4 = idle
 elif event_number == 5:
  check = 1
  print('tosleep')
  window.after(100,update,cycle,check,event_number,x) #no. 5 = idle to sleep
 elif event_number in walk_left:
  check = 4
  print('walkingleft')
  window.after(100,update,cycle,check,event_number,x)#no. 6,7 = walk towards left
 elif event_number in walk_right:
  check = 5
  print('walkingright')
  window.after(100,update,cycle,check,event_number,x)#no 8,9 = walk towards right
 elif event_number in sleep_num:
  check  = 2
  print('sleep')
  window.after(1000,update,cycle,check,event_number,x)#no. 10,11,12,13,15 = sleep
 elif event_number == 14:
  check = 3
  print('toidle')
  window.after(100,update,cycle,check,event_number,x)#no. 15 = sleep to idle
#making gif work 
def gif_work(cycle,frames,event_number,first_num,last_num):
 if cycle < len(frames) -1:
  cycle+=1
 else:
  cycle = 0
  event_number = random.randrange(first_num,last_num+1,1)
 return cycle,event_number
def update(cycle,check,event_number,x):
 #idle
 if check ==0:
  frame = idle[cycle]
  cycle ,event_number = gif_work(cycle,idle,event_number,1,9)
  
 #idle to sleep
 elif check ==1:
  frame = tosleep[cycle]
  cycle ,event_number = gif_work(cycle,tosleep,event_number,10,10)
#sleep
 elif check == 2:
  frame = sleep[cycle]
  cycle ,event_number = gif_work(cycle,sleep,event_number,10,15)
#sleep to idle
 elif check ==3:
  frame = toidle[cycle]
  cycle ,event_number = gif_work(cycle,toidle,event_number,1,1)
#walk toward left
 elif check == 4:
  frame = walkingleft[cycle]
  cycle , event_number = gif_work(cycle,walkingleft,event_number,1,9)
  x -= 3
#walk towards right
 elif check == 5:
  frame = walkingright[cycle]
  cycle , event_number = gif_work(cycle,walkingright,event_number,1,9)
  x -= -3
 window.geometry('150x150+'+str(x)+'x'+str(y)) #change x and y depending on screen size
 label.configure(image=frame)
 window.after(1,event,cycle,check,event_number,x)
window = tk.Tk()
#call buddy's action gif
idle = [tk.PhotoImage(file=impath+'/idle.gif',format = 'gif -index %i' %(i)) for i in range(12)]#idle gif
tosleep = [tk.PhotoImage(file=impath+'/tosleep.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle to sleep gif
sleep = [tk.PhotoImage(file=impath+'/sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]#sleep gif
toidle = [tk.PhotoImage(file=impath+'/toidle.gif',format = 'gif -index %i' %(i)) for i in range(5)]#sleep to idle gif
walkingleft = [tk.PhotoImage(file=impath+'/walkingleft.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to left gif
walkingright = [tk.PhotoImage(file=impath+'/walkingright.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to right gif
#window configuration
window.config(highlightbackground='white')
label = tk.Label(window,bd=0,bg='white', text="TEST")
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','white')

label.pack()
#loop the program
window.after(1,update,cycle,check,event_number,x)
window.mainloop()
