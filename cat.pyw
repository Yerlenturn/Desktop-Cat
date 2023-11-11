import pyautogui
import random
import tkinter as tk
import webbrowser
import subprocess
import json
from datetime import datetime as dt


idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = 'C:\\Users\\flynn\\OneDrive\\Desktop\\pe\\images\\'
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
subprocess.Popen(["node", "todoList\\server.js"], shell=True)

fin = []
unfin = []
rem = ""
nextTask = "Nothing!!!"
today = dt.today()
print(today)
def gettasks():
  global fin, unfin, rem, nextTask, today
  f = open('todoList\\notes\\toDoList.json')
  jdata = json.load(f)
  f.close()
  tasks = [i for i in jdata["tasks"]]
  fin = [jdata["tasks"][i] for i in tasks if jdata["tasks"][i]["done"]]
  unfin = [jdata["tasks"][i] for i in tasks if not jdata["tasks"][i]["done"]]
  rem = jdata["reminder"]
  if len(unfin) > 0: 
    nextTask = unfin[0]
    for i in unfin:
      ti =dt.strptime(i["date"], '%Y-%m-%d')
      ni = dt.strptime(nextTask["date"], '%Y-%m-%d')
      if ti < ni and ti > today:
        nextTask = i
    nextTask = nextTask["task"]
  else: nextTask = "Nothing!!!"




class Main(tk.Frame):
  def __init__(self, master):
    tk.Frame.__init__(self, master)
    self.textbox = [tk.PhotoImage(file=impath+'textbox.gif',format = 'gif -index %i' %(i)) for i in range(7)]#idle gif
    self.x = self.px = 1400
    self.cycle = 0
    self.check = 1


class pet(tk.Tk):
  def __init__(self):
    super().__init__()
    
    self.idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle gif
    self.idle_to_sleep = [tk.PhotoImage(file=impath+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]#idle to sleep gif
    self.sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]#sleep gif
    self.sleep_to_idle = [tk.PhotoImage(file=impath+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]#sleep to idle gif
    self.walk_positive = [tk.PhotoImage(file=impath+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to left gif
    self.walk_negative = [tk.PhotoImage(file=impath+'walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to right gif
    #window configuration
    self.config(highlightbackground='black')
    self.label = tk.Label(self,bd=0,bg='black')
    self.overrideredirect(True)
    self.wm_attributes('-transparentcolor','black')
    self.attributes('-topmost', True)
    self.label.pack()
    
    #other frames
    self.rems = None

# Bindings
    self.label.bind('<Button-1>', self.on_click)
    self.label.bind('<Enter>', self.on_hover)
    self.label.bind('<Leave>', self.off_hover)
    self.window = Main(self)
    self.window.pack()
    self.after(1, self.update, self.window.cycle, self.window.check, event_number, self.window.x)
    #self.mainloop()

#call buddy's action gif
  #def popup(self):
  #  Popup(self)
  def on_click(self, event=None):
    webbrowser.get(chrome_path).open('file:///C:/Users/flynn/OneDrive/Desktop/pe//todoList/index.html')
  
  def on_hover(self, event=None):
    if self.rems == None: self.rems = Rems(self.window)
    self.window.check = -1

  def off_hover(self, event=None):
    if self.rems != None: self.rems.kill()
    self.rems = None
    self.window.check = 0

  def win(self):
    return "ASS"
  #transfer random no. to event
  def event(self,cycle,check,event_number,x):
    if event_number in idle_num and check != -1:
      self.window.check = 0
      #print('idle')
      self.after(400,self.update,self.window.cycle,self.window.check,event_number,self.window.x) #no. 1,2,3,4 = idle
    elif event_number == 5 and check != -1:
      self.window.check = 1
      #print('from idle to sleep')
      self.after(100,self.update,self.window.cycle,self.window.check,event_number,self.window.x) #no. 5 = idle to sleep
    elif event_number in walk_left and check != -1:
      self.window.check = 4
      #print('walking towards left')
      self.after(100,self.update,self.window.cycle,self.window.check,event_number,self.window.x)#no. 6,7 = walk towards left
    elif event_number in walk_right and check != -1:
      self.window.check = 5
      #print('walking towards right')
      self.after(100,self.update,self.window.cycle,self.window.check,event_number,self.window.x)#no 8,9 = walk towards right
    elif event_number in sleep_num and check != -1:
      self.window.check  = 2
      #print('sleep')
      self.after(1000,self.update,self.window.cycle,self.window.check,event_number,self.window.x)#no. 10,11,12,13,15 = sleep
    elif event_number == 14 and check != -1:
      self.window.check = 3
      #print('from sleep to idle')
      self.after(100,self.update,self.window.cycle,self.window.check,event_number,self.window.x)#no. 15 = sleep to idle
    else: self.after(400,self.update,self.window.cycle,self.window.check,event_number,self.window.x) #no. 1,2,3,4 = idle
  #making gif work 
  def gif_work(self,cycle,frames,event_number,first_num,last_num):
    if cycle < len(frames) -1:
      cycle+=1
    else:
      cycle = 0
      event_number = random.randrange(first_num,last_num+1,1)
    return cycle,event_number
  def update(self,cycle,check,event_number,x):
  #idle
    if check ==0 or check == -1:
      try:
        frame = self.idle[cycle]
      except:
        frame = self.idle[0]
      self.window.cycle ,event_number = self.gif_work(cycle,self.idle,event_number,1,9)
    
  #idle to sleep
    elif check ==1:
      frame = self.idle_to_sleep[cycle]
      self.window.cycle ,event_number = self.gif_work(cycle,self.idle_to_sleep,event_number,10,10)
  #sleep
    elif check == 2:
      try:
        frame = self.sleep[cycle]
      except:
        frame = self.sleep[0]
      self.window.cycle ,event_number = self.gif_work(cycle,self.sleep,event_number,10,15)
  #sleep to idle
    elif check ==3:
      frame = self.sleep_to_idle[cycle]
      self.window.cycle ,event_number = self.gif_work(cycle,self.sleep_to_idle,event_number,1,1)
  #walk toward left
    elif check == 4:
      frame = self.walk_positive[cycle]
      self.window.cycle , event_number = self.gif_work(cycle,self.walk_positive,event_number,1,9)
      self.window.x -= 3
      self.window.px -= 3
  #walk towards right
    elif check == 5:
      frame = self.walk_negative[cycle]
      self.window.cycle , event_number = self.gif_work(cycle,self.walk_negative,event_number,1,9)
      self.window.x -= -3
      self.window.px -= -3

    self.geometry('100x100+'+str(x)+'+1050')
    self.label.configure(image=frame)
    self.after(1,self.event,self.window.cycle,self.window.check,event_number,self.window.x)

class Rems(tk.Toplevel):
  def __init__(self, master):
    tk.Toplevel.__init__(self, master)
    #panel = [tk.PhotoImage(file=impath+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(4)]
    self.config(highlightbackground='black')
    self.wm_attributes('-transparentcolor','black')
    self.l = tk.Label(self,bd=0,bg='black')
    self.uf = tk.Label(self, text="Please shit yourself", bg='#fed2d2',fg="purple", font=("MS PGothic", 12))
    self.nt = tk.Label(self, text="Please shit yourself", bg='#fed2d2',fg="purple", font=("MS PGothic", 12), wraplength=300)
    self.r = tk.Label(self, text="Please shit yourself", bg='#fed2d2',fg="purple", font=("MS PGothic", 12), wraplength=170)
    self.cycle = 0

    self.overrideredirect(True)
    self.attributes('-topmost', True)
    self.geometry('300x223+'+str(master.px - 200)+'+880')

    self.l.pack()
    self.uf.pack(expand= True, padx=0, pady=10)
    self.nt.pack(expand= True, padx=0, pady=10)
    self.r.pack(expand= True, padx=0, pady=10)
    gettasks()
    self.tupdate(master, self.cycle)
    self.update_idletasks()

  def tupdate(self, master, cycle):
    if self.cycle < len(master.textbox) -1:
      self.cycle += 1
    else:
      self.cycle = 0
    frame = master.textbox[cycle]
    #self.geometry('300x223+'+str(master.px - 200)+'+880')
    self.l.configure(image=frame)
    self.uf.configure(text=f"Tasks Not Finished: {len(unfin)}")
    self.nt.configure(text=f"Next Task: {nextTask}")
    self.r.configure(text=f"Reminder: {rem}")
    self.uf.place(relx=0.4, rely=0.1, anchor='center')
    self.nt.place(relx=0.4, rely=0.2, anchor='center')
    self.r.place(relx=0.5, rely=0.4, anchor='center')
    master.master.after(100, self.tupdate, master, self.cycle)

		
  def kill(self):
    self.destroy()


if __name__ == "__main__":
  Buddy = pet()
  Buddy.mainloop()
